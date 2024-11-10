<p>
    <a title="Visit The Kimchi Reader Website" href="https://kimchi-reader.app/">
        <img src="https://img.shields.io/badge/Website-Kimchi%20Reader-darkred">
    </a>
      <a title="Join The Discord Server" href="https://discord.gg/ctHcGSrgra">
        <img src="https://img.shields.io/badge/Discord-Join%20The%20Kimchi%20Reader%20Discord-7289DA?logo=discord&logoColor=white">
    </a>
    <a title="License: Apache License 2.0" href="https://github.com/seulgiism/Kimchi-Reader-Discord-Bot/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg">
    </a>
</p>

# Kimchi Reader Discord Bot

The **Kimchi Reader Discord Bot** enhances the experience of members in the Kimchi Reader Discord server by sending personalized welcome messages, providing helpful links in DMs, and offering interactive commands. 
This bot is community-maintained.

# Installation

### Prerequisites

- **Python 3.8 or higher** installed on your system.
- A **Discord Bot Token** from the [Discord Developer Portal](https://discord.com/developers/applications).
- Python Libraries: see requirements.txt file.

### Steps

1. **Clone the Repository**

   ```
   git clone https://github.com/seulgiism/Kimchi-Reader-Discord-Bot.git
   cd Kimchi-Reader-Discord-Bot
   ```

2. **Create a Virtual Environment (Recommended)**

   ```
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On macOS/Linux:

     ```
     source venv/bin/activate
     ```

   - On Windows:

     ```
     venv\Scripts\activate
     ```

4. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

5. **Obtain a Discord Bot Token**

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click **"New Application"** and give it a name.
   - Navigate to the **"Bot"** tab and click **"Add Bot"**.
   - Click **"Reset Token"** to generate your bot token. **Keep this token secure!**

6. **Configure the Bot Token**

   **Option A: Use Environment Variables**

   - Set the environment variable in your terminal:

     - On macOS/Linux:

       ```
       export DISCORD_BOT_TOKEN='YOUR_BOT_TOKEN_HERE'
       ```

     - On Windows:

       ```
       set DISCORD_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
       ```

   **Option B: Use a `.env` File**

   - Install `python-dotenv`:

     ```
     pip install python-dotenv
     ```

   - Create a file named `.env` in the project directory and add:

     ```
     DISCORD_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
     ```
     
7. **Set Up the Bot in the Developer Portal**

   - **Bot Permissions:**

     - Under the **"Bot"** tab, enable the following intents:

       - **Server Members Intent** (required for welcome messages)
       - **Message Content Intent** (if your bot needs to read message content)

   - **OAuth2 Settings:**

     - Go to the **"OAuth2"** > **"URL Generator"**.
     - Select the scopes:

       - `bot`
       - `applications.commands`

     - Under **"Bot Permissions"**, select:

       - **Send Messages**
       - **Embed Links**
       - **Read Message History**
       - **Use Slash Commands**

     - Copy the generated URL and invite the bot to your Discord server using this link.

8. **Run the Bot**

   ```
   python kimchi_reader_bot.py
   ```

## Contributing

Contributions of all kinds are welcome! Whether you're fixing bugs, adding new features, or improving documentation, your help is appreciated. Please make sure that your contributions:

- **Does not spam** the server.
- **Comply with Discord's Terms of Service**.

Thank you for contributing to the Kimchi Reader Discord Bot!
