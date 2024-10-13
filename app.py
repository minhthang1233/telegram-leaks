import os
import asyncio
from telethon import TelegramClient, events

# Lấy thông tin từ biến môi trường
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
phone = os.environ['PHONE_NUMBER']

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)  # Sử dụng phone từ biến môi trường

    @client.on(events.NewMessage(chats='t.me/thutele1234'))
    async def handler(event):
        # Gửi tin nhắn đến nhóm nhận
        await client.send_message('t.me/thutele12344', event.message)

    print("Bot đang chạy...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
