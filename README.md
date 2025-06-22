# Multipurpose Discord Selfbot

A multipurpose Discord selfbot with moderation, utility, and fun commands.  
**For educational and personal use only.**

## Features

- Moderation: kick, ban, unban, clear, massdm, massreact, banall, nuke, nickname, addrole, removerole
- Utility: ping, spam, avatar, serverinfo, calc, afk, unafk, join/leave voice channel
- Fun: jokes, fake nitro, hack profile, tribute, and more
- Custom commands for payments and server info

## Requirements

- Python 3.8+
- Discord account (for selfbot usage)
- All dependencies listed in `requirements.txt`

## Setup

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd "Voce host project"
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   - Create a `.env` file in the project root:
     ```
     TOKEN=your_discord_token_here
     PREFIX=!
     ```
   - Replace `your_discord_token_here` with your Discord account token.
   - Set your desired command prefix.

4. **Run the selfbot:**
   ```sh
   python main.py
   ```

## Usage

- Use commands in Discord chat with your chosen prefix.
- Example: `!ping`, `!kick @user`, `!joinvc #voice-channel`

## Important Notes

- **Selfbots are against Discord's Terms of Service.**  
  Use at your own risk. This project is for educational purposes only.
- Make sure your account is secure and you understand the risks before running a selfbot.

## License

This project is provided for educational purposes.  
No warranty is provided. Use responsibly.
