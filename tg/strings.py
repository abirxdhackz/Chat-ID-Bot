default_lang = None

TEXT = {
    "WELCOME": {
        "en": "Welcome {name} \n\n"
        " In this bot you can get the ID of any group, channel, user, or bot\n\n"
        " To use the bot, click on the buttons below and share the chat whose ID you want to know."
        " - In response, the bot will return the ID of the chat you shared\n\n"
        ">  To change the language send the /lang command\n\n"
        ">  You can get the ID in many other ways. Send the /help command\n\n"
        ">  Want to donate to me? Send the /donate command\n\n"
        " For updates on the bot, subscribe to @abir_x_official"
    },
    "USER": {"en": "👤 User"},
    "BOT": {"en": "🤖 Bot"},
    "CHANNEL": {"en": "📢 Channel"},
    "GROUP": {"en": "👥 Group"},
    "ID_USER": {"en": "🆔 The ID of {} is: `{}`"},
    "ID_USERS": {"en": "🆔 The IDs of: \n{}"},
    "ID_CHANNEL_OR_GROUP": {"en": "📢 The ID of {} is: `{}`"},
    "ID_CHANNELS_OR_GROUPS": {"en": "📢 The IDs of: \n{}"},
    "ID_HIDDEN": {"en": "🤫 The ID is hidden. \n{name}"},
    "CHOICE_LANG": {"en": "🌐 Select your language."},
    "DONE": {"en": "✅ The selected language is {}"},
    "NOT_HAVE_ID": {"en": "⚠️ The contact you sent has no ID."},
    "CAN_NOT_GET_THE_ID": {"en": "❌ It is not possible to get the ID of this chat."},
    "CHAT_MANAGER": {
        "en": "🔧 By clicking the buttons below, you can see all the groups and channels you manage and get their IDs."
    },
    "REQUEST_CHAT": {"en": "📩 Request Chat"},
    "INFO_REQUEST_CHAT": {
        "en": "**📩 Request Chat**\n\n"
        "🔘 Click on the buttons below and share the chat whose ID you want to know."
        "\n✅ In response, the bot will return the ID of the chat you shared."
    },
    "FORWARD": {"en": "📤 Forward"},
    "INFO_FORWARD": {
        "en": "**📤 Forward Message**\n\n"
        "🔄 Forward any message to the bot (forward with quotes), "
        "and the bot will return the ID of the chat from which the message was sent."
    },
    "STORY": {"en": "📖 Story"},
    "INFO_STORY": {
        "en": "**📖 Story**\n\n"
        "🎥 Transfer a story, and the bot will return its ID."
    },
    "SEARCH_USERNAME": {"en": "🔍 Username"},
    "INFO_SEARCH_USERNAME": {
        "en": "**🔍 Search by Username**\n\n"
        "📎 Send the username to the bot, and the bot will return the ID of the chat with that username."
    },
    "REPLY_TO_ANOTHER_CHAT": {"en": "📥 Reply to"},
    "INFO_REPLY_TO_ANOTHER_CHAT": {
        "en": "**📥 Reply to Another Chat**\n\n"
        "💬 Reply to any message in another chat, "
        "and the bot will return the ID of the chat from which the message was replied."
    },
    "CONTACT": {"en": "📇 Contact"},
    "INFO_CONTACT": {
        "en": "**📇 Contact**\n\n"
        "📱 Share a contact with the bot, and the bot will return the contact's ID to you."
    },
    "REQUEST_ADMIN": {"en": "🛠️ Admin"},
    "INFO_REQUEST_ADMIN": {
        "en": "**🛠️ Request Admin**\n\n"
        "🔧 Send the command `/admin` to get all the chats where you have name management."
    },
    "ME": {"en": "🙋‍♂️ Me"},
    "INFO_ME": {
        "en": "**🙋‍♂️ Get Your ID**\n\n"
        "🆔 Send the command `/me` to get your ID."
    },
    "LANGUAGE": {"en": "🌐 Language"},
    "INFO_LANGUAGE": {
        "en": "**🌐 Language**\n\n"
        "🗣️ To change the language, send the `/lang` command."
    },
    "INFO_GROUP": {
        "en": "**👥 Group**\n\n"
        "➕ Add the bot to the group with the command `/add`, "
        "and get the ID of the group members with the command `/id`."
    },
    "SHOW_ALL": {"en": "📋 Show all"},
    "NEXT": {"en": "Next ➡️"},
    "BACK": {"en": "⬅️ Back"},
    "MENU": {"en": "📜 Menu"},
    "INFO_MENU": {"en": "📜 Menu help"},
    "ABOUT": {"en": "ℹ️ About"},
    "INFO_ABOUT": {
        "en": "ℹ️ **Details about the bot**\n\n"
        "Language: [Python](https://www.python.org/) \n"
        "Library: [pyrotgfork](https://telegramplayground.github.io/pyrogram/) \n"
        "Bot creator: @abirxdhackz 👨‍💻\n\n"
        "Donations: You can support the bot creator with the /donate command\n\n"
        "The bot is open source on GitHub 🌟\n"
        "https://github.com/abirxdhackz/Chat-ID-Bot\n\n"
        "📢 For updates on the bot, subscribe to @abir_x_official."
    },
    "BUTTON_DEV": {"en": "Send message 👨‍💻"},
    "LINK_DEV": {"en": "https://t.me/abirxdhackz"},
    "CHOSE_CHAT_TYPE": {"en": "Choose chat type"},
    "BUTTON_ADD_BOT_TO_GROUP": {"en": "Add bot to group"},
    "ADD_BOT_TO_GROUP": {
        "en": "**Add bot to group**\n\n"
        "Click on the button to add the bot to the group to get IDs of members in the group."
    },
    "BOT_ADDED_TO_GROUP": {
        "en": "**Bot added to group**\n\n"
        "The bot was added to the group {group_name} ➡️ `{group_id}`.\n"
        "To get IDs of members in the group, send the command `/id` in the group."
    },
    "BUSINESS": {"en": "➡️ Business connection"},
    "INFO_BUSINESS": {
        "en": "**➡️ Business connection**\n\n"
        "You can connect the bot to your business and get the ID of any chat."
        "\n> Go to settings > Telegram Business > Chatbot > and select this bot."
        "\nThen you can send the command `.id` in any private chat to get the chat ID."
        "\nYou can also get the ID without sending a message in the chat!"
        "\n> Go to the chat and then click on the bot management button "
        "and the bot will send the ID of the chat you came from."
    },
    "BUSINESS_CONNECTION": {
        "en": "**➡️ Business connection**\n"
        "Hi, thanks for connecting with me! "
        "\nYou can use me by sending the command `.id` "
        "in any chat (private) to get the chat ID."
        "\n> You can also get the ID without sending a message in the chat!"
        "\n> Go to the chat and then click on the bot management button "
        "and the bot will send the ID of the chat you came from."
    },
    "BUSINESS_CONNECTION_DISABLED": {
        "en": "**➡️ Business Connection**\n"
        "🚫 I'm sorry, but I can't reply to your messages. "
        "💬 If you want to get the chat ID, please enable the permission to reply to messages."
    },
    "BUSINESS_CONNECTION_REMOVED": {
        "en": "**➡️ Business Connection**\n"
        "👋 I'm sorry to see you go, but I'm always here if you need me!"
    },
    "ID_BY_MANAGE_BUSINESS": {
        "en": "🎉 The ID of the chat you came from is: `{}`"
    },
    "ASK_AMOUNT_TO_PAY": {
        "en": "💖 Hi, thanks for wanting to donate to me 😊\n"
        "💰 Choose the donation amount you want to give 👇"
    },
    "SUPPORT_ME": {
        "en": "🙏 Support Me"
    },
    "TEXT_SUPPORT_ME": {
        "en": "✨ Support me with {} ✨"
    },
    "PAYMENT_SUCCESS": {
        "en": "🎉 Thank you for your donation 🎉\n"
        "💖 I received your generous donation of {} ✨"
    },
    "SOMTHING_WENT_WRONG": {
        "en": "⚠️ Oops! Something went wrong."
    },
    "LINK_TO_CHAT": {
        "en": "➡️ Link to Chat: `{}`"
    },
    "BUTTON_GET_LINK": {
        "en": "➡️ Get Link to Chat"
    },
    "FORMAT_LINK": {
        "en": "📋 Send the command with the chat ID.\n"
        "For example:\n> `/link 777000`"
    }
}

def get_text(*, key: str, lang: str) -> str:
    """
    Retrieve text based on a given key and language.
    Defaults to English ('en') if the key or language is unavailable.
    """
    # Default to a specific language if set
    if default_lang is not None:
        lang = default_lang
    else:
        lang = lang if lang == "he" else "en"  # Default to English if not "he"

    try:
        # Attempt to retrieve the text for the specified key and language
        if isinstance(TEXT[key], dict):
            return TEXT[key].get(lang, TEXT[key].get("en", "Missing text"))
        # Return the text directly if it is not a dictionary (assumes single-language key)
        return TEXT[key]
    except KeyError:
        # Fallback message if the key itself doesn't exist
        return f"Text not found for key: '{key}'."
