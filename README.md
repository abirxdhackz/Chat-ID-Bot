# 🤖 **Chat ID Bot**

## **Description**

**Chat ID Bot** is an advanced Telegram bot designed to effortlessly fetch IDs for users, bots, groups, and channels. Whether you're a developer, admin, or user, this bot makes retrieving Telegram IDs quick and easy!

_You can try the bot [here](https://t.me/Chat_ID_Adv_Bot).

_You can try the bot [here](https://t.me/Get_ID_Advanced_Bot).
---

## **Features**

- Retrieve **user IDs**, **bot IDs**, **group IDs**, and **channel IDs** with a simple command. 🔍
- Supports **private chats**, **group chats**, and **supergroups**. 📜
- Easy-to-use interface with inline buttons and fast responses. 🚀
- Multilingual support for a wider audience 🌍
- Admin controls to manage the bot’s functions 👮‍♂️

---

## **Setup**

### 1. Clone the Repository

Clone the repository to get started with the bot.

```bash
git clone https://github.com/abirxdhackz/Chat-ID-Bot.git
cd Chat-ID-Bot
```

---

### 2. Set Up Environment Variables

To configure the bot, you need to set up the environment variables.

1. **Copy the `.env.example` file:**

   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file:**

   Open the `.env` file in your preferred text editor and fill in your credentials:

   - **Telegram Credentials:**
     - `TELEGRAM_API_ID` and `TELEGRAM_API_HASH`: Obtain these from [my.telegram.org](https://my.telegram.org).
     - `TELEGRAM_BOT_TOKEN`: Create your bot via [BotFather](https://t.me/BotFather).
   - **Admin Settings:**
     - `ADMINS`: List of Telegram user IDs with admin privileges.

3. **Save the `.env` file.**

---

## **Installation**

Once your environment variables are configured, install dependencies and run the bot:

1. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the bot:
   ```bash
   python main.py
   ```

---

## **BotFather Commands**

You can configure and interact with the bot using the following commands in **BotFather**:

```txt
/start - Start the bot ✅
/lang - Change language 🇺🇸
/help - Get help 🆘
/me - View your profile 👤
/add - Add files ➕
/admin - Access admin panel 👮‍♂️
/about - Learn about the bot ℹ️
/donate - Support the bot 🙏
```

---

## **Usage**

- **Private Chats:** Start a conversation with the bot, and it will return your Telegram ID.
- **Groups and Channels:** Add the bot to a group or channel and use the `/id` command to get the group or channel’s ID.
- **Advanced Features:** Admins can retrieve detailed information about users or chats, and control bot settings via the admin panel.
- **Simple Bot.py:** This Script Is Another Simple Script But Advanced Bot.

### **Multilingual Support**

You can change the bot’s language using the `/lang` command to make it more accessible to a global audience.

---

## **Credits**

This project was created by [@yehudalev](https://github.com/yehuda-lev) and [@bisnuray](https://github.com/bisnuray), and developed and mixed or fixed by [@abirxdhackz](https://github.com/abirxdhackz).

---
