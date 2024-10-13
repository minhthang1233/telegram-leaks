import os
import asyncio
from telethon import TelegramClient, events

# Cấu hình API ID, API Hash và số điện thoại từ biến môi trường
api_id = os.environ.get('API_ID')  # Nhập API_ID
api_hash = os.environ.get('API_HASH')  # Nhập API_HASH
phone = os.environ.get('PHONE_NUMBER')  # Nhập PHONE_NUMBER
telegram_code = os.environ.get('TELEGRAM_CODE')  # Mã xác thực từ Telegram

# Kiểm tra xem các biến môi trường đã được thiết lập chưa
if not all([api_id, api_hash, phone]):
    raise ValueError("API_ID, API_HASH và PHONE_NUMBER phải được thiết lập trong biến môi trường.")

# Khởi tạo client Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Đăng nhập vào tài khoản Telegram
    await client.start(phone)

    # Lắng nghe các tin nhắn mới từ nhóm gốc
    @client.on(events.NewMessage(chats='t.me/thutele1234'))
    async def handler(event):
        # Lấy nội dung tin nhắn mới
        message = event.message.message
        # Gửi tin nhắn đến nhóm mới
        await client.send_message('t.me/thutele12344', message)

    print("Đang lắng nghe tin nhắn mới...")
    # Bắt đầu chạy client
    await client.run_until_disconnected()

# Chạy ứng dụng
if __name__ == '__main__':
    asyncio.run(main())
