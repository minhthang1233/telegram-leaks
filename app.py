import os
from telethon import TelegramClient

# Lấy thông tin từ biến môi trường
api_id = os.getenv('API_ID', '21357718')  # Thay thế bằng số ID của bạn
api_hash = os.getenv('API_HASH', 'df3564e279df7787a6292c45b177524a')  # Thay thế bằng mã hash của bạn
phone_number = os.getenv('PHONE_NUMBER', '+84367729142')  # Thay thế bằng số điện thoại của bạn

# Khởi tạo client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    print("Đăng nhập thành công")  # Kiểm tra xem đăng nhập có thành công không

    async for message in client.iter_messages('sanbanshopee', limit=10):  # Lấy 10 tin nhắn gần nhất
        if message.text:
            print(f"Đã lấy tin nhắn: {message.text}")  # Kiểm tra tin nhắn đã lấy
            modified_message = modify_links(message.text)
            print(f"Tin nhắn đã sửa đổi: {modified_message}")  # Kiểm tra tin nhắn đã sửa đổi
            await client.send_message('thutele12344', modified_message)  # Gửi tin nhắn vào nhóm đích
            print("Tin nhắn đã được gửi đi")  # Kiểm tra xem tin nhắn đã gửi thành công chưa

def modify_links(text):
    # Sửa đổi link trong tin nhắn nếu cần
    # Thay thế 'lazada.com' thành 'example.com', bạn có thể thay đổi theo ý muốn
    return text.replace('lazada.com', 'example.com')  

with client:
    client.loop.run_until_complete(main())
