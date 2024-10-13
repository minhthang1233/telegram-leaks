import os
import sqlite3
from flask import Flask, request, render_template
from telethon import TelegramClient, events, errors

# Thay đổi các thông số sau đây cho đúng
api_id = int(os.environ.get('API_ID', '21357718'))  # Nhập API_ID
api_hash = os.environ.get('API_HASH', 'df3564e279df7787a6292c45b177524a')  # Nhập API_HASH
phone_number = os.environ.get('PHONE_NUMBER', '+84367729142')  # Nhập PHONE_NUMBER

app = Flask(__name__)
client = TelegramClient('session_name', api_id, api_hash)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_code', methods=['POST'])
def submit_code():
    code = request.form.get('code')
    try:
        # Bắt đầu client và đăng nhập
        with client:
            client.loop.run_until_complete(client.start())
            if not client.is_user_authorized():
                client.loop.run_until_complete(client.sign_in(phone_number, code))
                return "Đăng nhập thành công!"
            else:
                return "Bạn đã đăng nhập thành công trước đó."
    except errors.FloodWait as e:
        return f"Bạn đã bị giới hạn. Vui lòng thử lại sau {e.seconds} giây."
    except Exception as e:
        return f"Có lỗi xảy ra: {e}"

if __name__ == '__main__':
    app.run()
