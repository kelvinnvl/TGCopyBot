import os.path
import tempfile
from os import getenv
from sys import exit
from dotenv import load_dotenv, find_dotenv
from pyrogram import Client, raw, filters
import traceback

load_dotenv(find_dotenv())

# your key in https://my.telegram.org/auth?to=apps
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")

# Initialize the Pyrogram client
app = Client("my_session", api_id=API_ID, api_hash=API_HASH)

# Define the chat IDs for the source group/channel and the target supergroup
source_chat_id = getenv("SOURCE")  # Replace with the source chat ID
target_supergroup_id = getenv("DESTINATION")  # Replace with the target supergroup ID

# Define the topic ID within the supergroup
topic_id = 2  # Replace with the actual topic ID

# Filter messages from the source chat
@app.on_message(filters.chat(int(source_chat_id)))
async def forward_messages(client, message):
    try:
        # Send the original message to the supergroup
        await client.invoke(
            raw.functions.messages.ForwardMessages(
                from_peer = await client.resolve_peer(source_chat_id),
                to_peer = await client.resolve_peer(target_supergroup_id),
                id = [message.chat.id],
                top_msg_id = topic_id,
                random_id = [client.rnd_id()]
            )
        )
        print(f"Forwarded original message: {message.text}")
    except Exception as e:
        print(f"Error forwarding message: {e}")
        traceback.print_exc() 

# Start the client and listen for messages
app.run()
