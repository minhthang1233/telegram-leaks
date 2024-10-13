import os
from telethon import TelegramClient, events

# Lấy thông tin từ biến môi trường
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE_NUMBER')  # Thay vì yêu cầu nhập liệu

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    # Xử lý mã xác minh
    async def code_callback():
        return os.environ.get('VERIFICATION_CODE')  # Lấy mã từ biến môi trường

    client.sign_in(phone, code_callback=code_callback)

    # Logic lấy tin nhắn và gửi đi
    @client.on(events.NewMessage(chats='t.me/thutele1234'))
    async def handler(event):
        message = event.message.message
        await client.send_message('t.me/thutele12344', message)

    print("Bot đang chạy...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
