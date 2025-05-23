from telethon import TelegramClient, events
from telethon.sessions import StringSession
from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

api_id = getenv("API_ID")
api_hash = getenv("API_HASH")
session_string = getenv("SESSION_STRING")

source = [-1002129953530,-1001826070260,-1001924828244]

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(chats=(source)))
async def my_event_handler(event):
    # Replace 'to_supergroup_id' and 'top_msg_id' with your actual values
    to_peers = {
            int('-1002013334245'): '575',
            int('-1002027620537'): None,
            'Xxm0nsterxX': None
            }
    
    # Get the sender
    sender = await event.message.get_sender()

    # Check if the post_author attribute is available
    post_author = event.message.post_author 

    # Create a new message with the sender's name, post author's name (if available), and the original message text
    if post_author:
        new_message = f"頻道: {sender.title}\n來自: {post_author}\n{event.message.text}"
    else:
        new_message = f"頻道: {sender.title}\n{event.message.text}"


    # await client(functions.messages.ForwardMessagesRequest(
    #     from_peer=event.chat_id,
    #     id=[event.message.id],
    #     to_peer=to_peer,
    #     drop_author=True,
    #     random_id=[generate_random_long()],
    #     top_msg_id=int(top_msg_id)  # Convert to int if it's a string
    # ))

    # await client(SendMessageRequest(
    #     peer=to_peer,
    #     message=event.message.message,
    #     reply_to=top_msg_id
    # ))

    for to_peer_id, top_msg_id in to_peers.items():
            to_peer = await client.get_input_entity(to_peer_id)

            if top_msg_id is not None:
                # Check if the message has media
                if event.message.media:
                    await client.send_file(
                         entity=to_peer,
                         file=event.message.media,
                         caption=new_message,
                         reply_to=int(top_msg_id)  # Convert to int if it's a string
                    )
                else:
                    await client.send_message(
                        entity=to_peer,
                        message=new_message,
                        reply_to=int(top_msg_id)  # Convert to int if it's a string
                    )
            else:
                # Check if the message has media
                if event.message.media:
                    await client.send_file(
                         entity=to_peer,
                         file=event.message.media,
                         caption=new_message
                    )
                else:
                    await client.send_message(
                        entity=to_peer,
                        message=new_message
                    )

with client:
    client.run_until_disconnected()