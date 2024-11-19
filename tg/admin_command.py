import io
import logging
import random
import string
import tempfile
import asyncio  # Use asyncio for non-blocking sleep
from pyrogram import Client, types, errors

from db import repository
from tg import filters

_logger = logging.getLogger(__name__)

async def stats(_: Client, msg: types.Message):  # command /stats
    """
    Get the stats of the bot.
    """
    users = repository.get_all_users_count()
    users_active = repository.get_users_count_active()
    business = repository.get_users_business_count()

    groups = repository.get_all_groups_count()
    groups_active = repository.get_groups_count_active()

    text = (
        f"**Bot Statistics**\n"
        f"**The number of users subscribed to the bot are:** \n"
        f"Total: {users}\n"
        f"Active: {users_active}\n"
        f"Inactive: {users - users_active}\n"
        f"Business users: {business}\n\n"
        f"**The number of groups in the bot are:** \n"
        f"Total: {groups}\n"
        f"Active: {groups_active}\n"
        f"Inactive: {groups - groups_active}\n"
    )

    await msg.reply(text=text, quote=True)

async def ask_for_who_to_send(_: Client, msg: types.Message):
    """
    Ask the user to choose who they want to send a message to.
    """
    await msg.reply(
        text="Who would you like to send a message to?",
        quote=True,
        reply_markup=types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(
                        text="To all users", callback_data="send:users"
                    )
                ],
                [
                    types.InlineKeyboardButton(
                        text="To all groups",
                        callback_data="send:groups",
                    )
                ],
                [types.InlineKeyboardButton(text="Cancel", callback_data="send:no")],
            ]
        ),
    )

async def asq_message_for_subscribe(_: Client, msg: types.CallbackQuery):
    """
    Handle message sending options for users or groups based on the callback data.
    """
    match send_to := msg.data.split(":")[-1]:
        case "users":
            text = "all users"
        case "groups":
            text = "all groups"
        case "no":
            await msg.answer("The message will not be sent")
            await msg.message.edit_text("Canceled")
            return
        case _:
            return

    await msg.message.reply(
        text=f"Please send the message you would like to send to {text}\n"
        f"> If the message is sent with credit, the bot will also forward it with credit",
    )
    filters.add_listener(
        tg_id=msg.from_user.id,
        data={"send_message_to_subscribers": True, "data": send_to},
    )

async def send_broadcast(_: Client, msg: types.Message):
    tg_id = msg.from_user.id
    send_to: str = filters.user_id_to_state.get(tg_id).get("data")
    filters.user_id_to_state.pop(tg_id)

    match send_to:
        case "users":
            users = repository.get_all_users_active()
            chats = None
        case "groups":
            chats = repository.get_all_groups_active()
            users = None
        case _:
            return

    log_obj = io.StringIO()
    sent = 0
    failed = 0
    count = 0
    count_edit = 0

    while True:
        sent_id = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        if not repository.is_message_sent_exists(sent_id=sent_id):
            break

    await msg.reply(
        text=f"**📣 Starting to send to:** {len((chats if chats is not None else users))} chats\nPlease wait...\n"
        f"> Sending ID: `{sent_id}` You can use it to delete the sent messages with the command `/delete {sent_id}`",
    )

    progress = await msg.reply(text=f"**Message sent to:** {sent} chats")

    if users is not None:  # send to users
        for user in users:
            if count > 40:
                count = 0
                await asyncio.sleep(3)  # Non-blocking sleep
            try:
                if msg.forward_origin:
                    msg_sent = await msg.forward(chat_id=user.tg_id)
                else:
                    msg_sent = await msg.copy(chat_id=user.tg_id)
                sent += 1

                repository.create_message_sent(
                    sent_id=sent_id, chat_id=user.tg_id, message_id=msg_sent.id
                )

                # Log success
                text_log = (
                    f"sent to user: {user.tg_id}, name: {user.name}, "
                    f"language_code: {user.language_code}, username: {user.username}\n"
                )
                log_obj.write(text_log)
                _logger.debug(text_log)

                # Update progress every 10 messages sent
                if sent % 10 == 0:
                    await progress.edit_text(
                        text=f"**The message has been sent to:** {sent} chats",
                    )

                count += 1
                await asyncio.sleep(0.05)  # Non-blocking sleep

            except errors.FloodWait as e:
                _logger.error(f"FloodWait: {e.value}")
                await asyncio.sleep(e.value)

            except errors.InputUserDeactivated:
                repository.update_user(tg_id=user.tg_id, active=False)
                text_log = (
                    f"user {user.tg_id}, name: {user.name} "
                    f"language_code: {user.language_code}, username: {user.username} is Deactivated\n"
                )
                log_obj.write(text_log)
                _logger.debug(text_log)
                failed += 1

            except errors.UserIsBlocked:
                repository.update_user(tg_id=user.tg_id, active=False)
                text_log = (
                    f"user {user.tg_id}, name: {user.name} "
                    f"language_code: {user.language_code}, username: {user.username} Blocked your bot\n"
                )
                log_obj.write(text_log)
                _logger.debug(text_log)
                failed += 1

            except errors.PeerIdInvalid:
                repository.update_user(tg_id=user.tg_id, active=False)
                text_log = (
                    f"user {user.tg_id}, name: {user.name} "
                    f"language_code: {user.language_code}, username: {user.username} IdInvalid\n"
                )
                log_obj.write(text_log)
                _logger.debug(text_log)
                failed += 1

            except errors.BadRequest as e:
                repository.update_user(tg_id=user.tg_id, active=False)
                text_log = (
                    f"BadRequest: {e} : user {user.tg_id}, name: {user.name} "
                    f"language_code: {user.language_code}, username: {user.username}"
                )
                log_obj.write(text_log)
                _logger.debug(text_log)
                failed += 1

    if chats is not None:  # send to chats
        for chat in chats:
            if count > 40:
                count = 0
                await asyncio.sleep(3)
            try:
                if msg.forward_origin:
                    msg_sent = await msg.forward(chat_id=chat.group_id)
                else:
                    msg_sent = await msg.copy(chat_id=chat.group_id)
                sent += 1

                repository.create_message_sent(
                    sent_id=sent_id, chat_id=chat.group_id, message_id=msg_sent.id
                )

                # Log success
                text_log = f"sent to chat: {chat.group_id}, name: {chat.name}, username: {chat.username}\n"
                log_obj.write(text_log)
                _logger.debug(text_log)

                # Update progress every 10 messages sent
                if sent % 10 == 0:
                    await progress.edit_text(
                        text=f"**ההודעה נשלחה ל:** {sent} צ'אטים",
                    )

                count += 1
                await asyncio.sleep(0.05)

            except errors.FloodWait as e:
                _logger.error(f"FloodWait: {e.value}")
                await asyncio.sleep(e.value)

            except errors.BadRequest as e:
                repository.update_group(group_id=chat.group_id, active=False)
                text_log = f"BadRequest: {e}, chat_id: {chat.group_id}, name: {chat.name}, username: {chat.username}"
                log_obj.write(text_log)
                _logger.debug(text_log)
                failed += 1

    # Send report at the end of the broadcast
    await send_report(_, msg, sent, failed, sent_id, log_obj, repository)

# Function to send a report message
async def send_report(client: Client, msg: types.Message, sent, failed, sent_id, log_obj, repository):
    text_done = (
        f"📣 Sending completed\n\n"
        f"🔹 The message was sent to: {sent} chats\n"
        f"🔹 The message failed in: {failed} chats"
        f"\n\n🔹 Sending ID: {sent_id}\n"
        f"🔹 Sent on: {time.strftime('%d/%m/%Y')}\n"
        f"🔹 Sent at: {time.strftime('%H:%M:%S')}\n"
        f"\nYou can delete the messages by sending the command `/delete {sent_id}`"
    )

    # Log the report
    text_log = f"\n\nSent: {sent}, Failed: {failed}\n Sent_id: {sent_id}\n\n"
    log_obj.write(text_log)
    _logger.debug(text_log)

    # Save log to a temporary file
    with tempfile.TemporaryFile(delete=False) as temp_file:
        # Write log to file
        temp_file.write(log_obj.getvalue().encode())
        temp_file.flush()
        temp_file_path = temp_file.name

        try:
            await msg.reply_document(document=temp_file_path, caption=text_done)
        except Exception as e:
            _logger.exception(e)
            await msg.reply(f"```py\n{e}```")

# Function to delete sent messages
async def delete_sent_messages(client: Client, msg: types.Message):
    """
    Delete sent messages.
    When the user sends the command /delete
    """
    try:
        sent_id = msg.text.split(" ")[1]
    except IndexError:
        await msg.reply("Message ID not found")
        return

    # Validate the sent ID
    if not repository.is_message_sent_exists(sent_id=sent_id):
        await msg.reply("The ID is not valid")
        return

    sent_messages = repository.get_messages_sent(sent_id=sent_id)
    await msg.reply(f"Deleting {len(sent_messages)} sent messages")

    count = 0
    delete = 0
    for sent_message in sent_messages:
        if count > 40:
            count = 0
            await asyncio.sleep(3)  # Non-blocking sleep after 40 messages

        try:
            await client.delete_messages(
                chat_id=sent_message.chat_id, message_ids=sent_message.message_id
            )
            count += 1
            await asyncio.sleep(0.05)
            delete += 1

        except errors.FloodWait as e:
            _logger.error(f"FloodWait: {e.value}")
            await asyncio.sleep(e.value)

        except Exception as e:
            _logger.error(
                f"Error: {e}, chat_id: {sent_message.chat_id}, message_id: {sent_message.message_id}"
            )

    await msg.reply(f"Deleted {delete} messages")
