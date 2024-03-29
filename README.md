# Discord Bro

## Description
The Discord Bro is a helpful bro that provides assistance and performs various tasks in a Discord server. It is built using the Discord.py library and the OpenAI GPT-3 language model.

## Features
- Chat with the bot by sending messages starting with "$".
- The bot can handle text messages as well as file attachments.
- Supports voice messages by converting the bot's response to speech.
- Utilizes the OpenAI GPT-3 language model to generate intelligent responses.
- Provides functions to fetch the current date and time, browse web content, and search for GIFs.
- Easy-to-use and customizable for your own server.

## Installation
1. Clone the repository:

git clone https://github.com/ninjahuttjr/brother.git

2. Install the required dependencies:

discord.py: A Python library for interacting with the Discord API. It provides an easy-to-use interface for creating Discord bots and handling events.

openai: A Python library for accessing the OpenAI API. It allows you to make requests to the OpenAI GPT-3 language model and retrieve generated responses.

dotenv: A Python library for loading environment variables from a .env file. It helps in securely storing sensitive information such as API keys.

requests: A Python library for making HTTP requests. It is used for fetching web content and interacting with the GIPHY API.

beautifulsoup4: A Python library for parsing HTML and XML documents. It is used for extracting text content from webpages fetched using the requests library.

python-dotenv: A Python library for parsing .env files. It is used for loading environment variables from a .env file into the project.

ffmpeg-python: A Python library for handling audio and video files. It is used for playing the voice responses generated by the bot.



pip install -r requirements.txt


3. Create a `.env` file in the project directory and add the following environment variables:

DISCORD_BOT_TOKEN=<your-discord-bot-token>
OPENAI_API_KEY=<your-openai-api-key>
GIPHY_API_KEY=<your-giphy-api-key>

4. Run the bot:

python main.py


## Usage
Invite the bot to your Discord server.
Type "$" followed by your message to interact with the bot.
The bot will respond with text messages or voice messages if you are in a voice channel.

## Contributing-
Contributions are welcome! If you'd like to contribute to the project, please follow these
