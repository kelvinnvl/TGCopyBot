from dotenv import load_dotenv, find_dotenv
from os import getenv
from sys import exit
import asyncio
import telegram

load_dotenv(find_dotenv())

# Replace 'YOUR_TOKEN', 'YOUR_CHANNEL_ID', and 'YOUR_GROUP_ID' with actual values
API_TOKEN = getenv("BOT_TOKEN")
SOURCE = getenv("SOURCE")
DESTINATION = getenv("DESTINATION")

async def main():
    bot = telegram.Bot(API_TOKEN)
    async with bot:
        await bot.send_message(text='Hi John!', chat_id=619219376)

if __name__ == '__main__':
    asyncio.run(main())