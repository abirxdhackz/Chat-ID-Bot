from pyrogram import Client, filters
from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup, RequestPeerTypeChat, RequestPeerTypeUser, RequestPeerTypeChannel

API_ID = "42224323"
API_HASH = "b973424ggf8962b20113113f84efsbf6"
BOT_TOKEN = "234209420943209ANJNJDNAUUNFUNWUDNUND34"

bot = Client("quickinfo_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

menu_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                "Chats",
                request_chat=RequestPeerTypeChat(
                    button_id=1,
                    max=1
                )
            ),
            KeyboardButton(
                "Channels",
                request_chat=RequestPeerTypeChannel(
                    button_id=3,
                    max=1
                )
            )
        ],
        [
            KeyboardButton(
                "Bots",
                request_user=RequestPeerTypeUser(
                    button_id=2,
                    is_bot=True,
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True
                )
            ),
            KeyboardButton(
                "Users",
                request_user=RequestPeerTypeUser(
                    button_id=4,
                    is_bot=False,
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True
                )
            )
        ]
    ],
    resize_keyboard=True
)

@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply_text(
        "Welcome to Cʜᴀᴛ ID Fɪɴᴅᴇʀ! Choose an option below to get user, bot, group, or channel info:",
        reply_markup=menu_buttons
    )

@bot.on_message(filters.private)
async def handle_message(bot, message):
    if getattr(message, "chats_shared", None):
        if hasattr(message.chats_shared, "chats") and message.chats_shared.chats:
            for chat in message.chats_shared.chats:
                chat_id = chat.chat_id
                chat_name = chat.name
                chat_type = str(chat.chat_type).replace("ChatType.", "").capitalize()
                await message.reply_text(
                    f"**Shared Chat Info**\n"
                    f"Type: `{chat_type}`\n"
                    f"ID: `{chat_id}`\n"
                    f"Name: `{chat_name}`"
                )
        elif hasattr(message.chats_shared, "users") and message.chats_shared.users:
            for user in message.chats_shared.users:
                user_id = user.user_id
                first_name = user.first_name
                last_name = user.last_name or ""
                username = f"@{user.username}" if user.username else "No username"
                if user.username and user.username.lower().endswith("bot"):
                    user_type = "Bot"
                else:
                    user_type = "User"
                await message.reply_text(
                    f"**Shared {user_type} Info**\n"
                    f"ID: `{user_id}`\n"
                    f"Name: `{first_name} {last_name}`\n"
                    f"Username: `{username}`"
                )
    else:
        await message.reply_text("Please use the provided buttons to share a group, bot, channel, or user.")

if __name__ == "__main__":
    bot.run()
