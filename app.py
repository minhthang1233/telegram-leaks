import os
import sqlite3
from time import sleep
from telethon import TelegramClient, events, errors

# Thay đổi các thông số sau đây cho đúng
api_id = int(os.environ.get('API_ID', '21357718'))  # Nhập API_ID
api_hash = os.environ.get('API_HASH', 'df3564e279df7787a6292c45b177524a')  # Nhập API_HASH
phone_number = os.environ.get('PHONE_NUMBER', '+84367729142')  # Nhập PHONE_NUMBER

# Hàm kết nối đến cơ sở dữ liệu với retry
def connect_with_retry(db_name, retries=3):
    for i in range(retries):
        try:
            conn = sqlite3.connect(db_name)
            conn.execute('PRAGMA busy_timeout = 30000')  # Thay đổi timeout
            return conn
        except sqlite3.OperationalError:
            if i < retries - 1:
                sleep(1)  # Chờ 1 giây trước khi thử lại
    raise Exception("Could not connect to database after multiple attempts.")

# Kết nối đến cơ sở dữ liệu SQLite
conn = connect_with_retry('session_db.sqlite')

# Khởi tạo client Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    
    try:
        # Nếu chưa đăng nhập, yêu cầu người dùng nhập mã xác thực
        if not await client.is_user_authorized():
            print("Vui lòng nhập mã xác thực nhận được từ Telegram.")
            code = input("Nhập mã xác thực: ")
            await client.sign_in(phone_number, code)
    except errors.FloodWait as e:
        print(f"Bạn đã bị giới hạn. Vui lòng thử lại sau {e.seconds} giây.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

    print("Đăng nhập thành công!")

# Chạy ứng dụng
with client:
    client.loop.run_until_complete(main())
