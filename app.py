import os
import asyncio
from telethon import TelegramClient, events

# Cấu hình API ID, API Hash và số điện thoại từ biến môi trường
api_id = os.environ.get('21357718')  # Nhập API_ID
api_hash = os.environ.get('df3564e279df7787a6292c45b177524a')  # Nhập API_HASH
phone = os.environ.get('+84367729142')  # Nhập số điện thoại

# Kiểm tra xem biến môi trường có tồn tại không
if api_id is None or api_hash is None or phone is None:
    raise ValueError("API_ID, API_HASH và PHONE_NUMBER phải được thiết lập trong biến môi trường.")

# Khởi tạo client Telegram với tính năng lưu trữ phiên
client = TelegramClient('session_name', int(api_id), api_hash)

async def main():
    # Bắt đầu client
    await client.start(phone)

    # Kiểm tra xem đã đăng nhập chưa
    if not await client.is_user_authorized():
        # Nếu chưa đăng nhập, gửi mã xác nhận
        print("Chưa đăng nhập, hãy nhập mã xác nhận.")
        code = os.environ.get('TELEGRAM_CODE')
        if code:
            try:
                await client.sign_in(phone, code)
                print("Đăng nhập thành công!")
            except Exception as e:
                print(f"Lỗi khi đăng nhập: {e}")
                return
        else:
            print("Mã xác nhận không có trong biến môi trường. Vui lòng nhập mã xác nhận lần đầu.")
            return

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
