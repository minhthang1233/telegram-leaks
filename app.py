import os
import asyncio
from telethon import TelegramClient, events

# Cấu hình API ID, API Hash và số điện thoại từ biến môi trường
api_id = int(os.environ.get('API_ID'))  # Nhập API_ID
api_hash = os.environ.get('API_HASH')  # Nhập API_HASH
phone = os.environ.get('PHONE_NUMBER')  # Nhập số điện thoại

# Khởi tạo client Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)
    
    # Lấy mã xác nhận từ biến môi trường
    code = os.environ.get('TELEGRAM_CODE')  # Biến môi trường chứa mã xác nhận
    if code:
        await client.sign_in(phone, code)
    else:
        print("Mã xác nhận không có trong biến môi trường.")

    # Lắng nghe tin nhắn mới từ nhóm nguồn
    @client.on(events.NewMessage(chats='t.me/thutele1234'))
    async def handler(event):
        message = event.message
        # Gửi tin nhắn đến nhóm đích
        await client.send_message('t.me/thutele12344', message.text)

    print("Đang lắng nghe tin nhắn mới từ nhóm...")
    await client.run_until_disconnected()

# Chạy hàm main
if __name__ == "__main__":
    asyncio.run(main())
