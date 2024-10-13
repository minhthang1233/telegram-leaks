import os
from telethon import TelegramClient
import logging

# Thiết lập logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Lấy thông tin từ biến môi trường
api_id = os.getenv('API_ID', '21357718')
api_hash = os.getenv('API_HASH', 'df3564e279df7787a6292c45b177524a')
phone_number = os.getenv('PHONE_NUMBER', '+84367729142')

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    logger.info("Đăng nhập thành công")

    try:
        async for message in client.iter_messages('thutele1234', limit=10):
            if message.text:
                logger.info(f"Đã lấy tin nhắn: {message.text}")
                modified_message = modify_links(message.text)
                logger.info(f"Tin nhắn đã sửa đổi: {modified_message}")
                await client.send_message('thutele12344', modified_message)
                logger.info("Tin nhắn đã được gửi đi")
    except Exception as e:
        logger.error(f"Có lỗi xảy ra: {e}")

def modify_links(text):
    return text.replace('lazada.com', 'example.com')

with client:
    client.loop.run_until_complete(main())
