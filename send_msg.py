from telethon import TelegramClient
import asyncio
from telethon.errors import FloodWaitError

# install telethon and asyncio or you can get run the command in terminal "pip install -r requirements.txt"

api_id = 'your api_id, you can get it from https://my.telegram.org'
api_hash = 'your api_hash, you can get it from https://my.telegram.org'
# login to https://my.telegram.org -> enter "API development tools" -> enter information in the top two,
# if you want, you can also enter in the rest, so you can get api_id and api_hash
phone_number = '+998777777777'  # your phone_number

client = TelegramClient('anon', api_id, api_hash)


async def main():
    await client.start(phone=phone_number)
    user = await client.get_me()
    print(f"Logged in as {user.first_name}")

    for _ in range(5):  # Write how many times you need to send in the range
        try:
            await client.send_message('recipient\'s phone number', 'your_message')
            await asyncio.sleep(0)
        except FloodWaitError as e:
            print(f"FloodWaitError: {e}")
            await asyncio.sleep(e.seconds)

    print("Messages sent!")


with client:
    client.loop.run_until_complete(main())
