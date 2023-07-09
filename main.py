from openai_chat import send_message
from text_to_speech import text_to_speech
import discord
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

intents = discord.Intents().all()
client = discord.Client(intents=intents)

message_log = [{
    "role": "system",
    "content": "You are a bro named Brosef, you live in Discord, and you are a helpful assistant. You are helping a user with their requests, and you can find up to date information by surfing the web. This is one example of the many functions you have."
}]

first_request = True

@client.event
async def on_ready():
    print('Bot is ready and connected to Discord!')
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"Received message: {message.content}")
    if message.author == client.user:
        return

    global message_log, first_request

    if message.content.startswith('$'):
        user_input = message.content[1:]
        print(f"Received command: {user_input}")
        message_log.append({"role": "user", "content": user_input})

        print("Message log: ", message_log)  # <-- Print the message log here

        async with message.channel.typing():
            print("Processing message.")
            response = send_message(message_log)

        print("Message processed.")
        message_log.append({"role": "assistant", "content": response})

        # Split the response into chunks of 2000 characters each
        response_chunks = [response[i:i+2000] for i in range(0, len(response), 2000)]

        for chunk in response_chunks:
            print("Sending response chunk.")
            await message.channel.send(chunk)
        
        # Check if the user is in a voice channel
        if message.author.voice:
            print("User is in a voice channel. Preparing to send voice message.")
            await text_to_speech(response, message)

        if user_input.lower() == "quit":
            print("Received quit command. Shutting down.")
            await message.channel.send("Goodbye!")
            message_log = [{
                "role": "system",
                "content": "You are a helpful assistant."
            }]
            first_request = True

client.run(os.environ.get("DISCORD_BOT_TOKEN3"))
