import os
import asyncio
from flask import Flask, request, render_template
from telethon import TelegramClient, events

app = Flask(__name__)

# Cấu hình API ID, API Hash và số điện thoại từ biến môi trường
api_id = os.environ.get('API_ID')  # Nhập API_ID
api_hash = os.environ.get('API_HASH')  # Nhập API_HASH
phone = os.environ.get('PHONE_NUMBER')  # Nhập PHONE_NUMBER

# Khởi tạo client Telegram
client = TelegramClient('session_name', api_id, api_hash)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
async def login():
    code = request.form['code']
    await client.start(phone)

    # Xác thực người dùng
    if not await client.is_user_authorized():
        try:
            await client.sign_in(phone, code)
            return "Đăng nhập thành công! Bây giờ bạn có thể lắng nghe tin nhắn."
        except Exception as e:
            return f"Lỗi: {str(e)}"

@app.route('/listen')
async def listen():
    @client.on(events.NewMessage(chats='t.me/thutele1234'))
    async def handler(event):
        message = event.message.message
        await client.send_message('t.me/thutele12344', message)

    print("Đang lắng nghe tin nhắn mới...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    app.run(debug=True)
