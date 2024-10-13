from telethon import TelegramClient, events
import os

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')

# Thay đổi tên nhóm để lấy tin nhắn và gửi tin nhắn
SOURCE_GROUP = 'sanbanshopee'  # Nhóm bạn muốn lấy tin nhắn
TARGET_GROUP = 'thutele12344'    # Nhóm bạn muốn gửi tin nhắn đến

client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_GROUP))
async def handler(event):
    # Lấy nội dung tin nhắn
    message_text = event.message.message
    
    # Nếu cần sửa đổi nội dung tin nhắn, có thể thực hiện ở đây
    modified_message = message_text  # Sửa đổi nếu cần
    
    # Gửi tin nhắn vào nhóm mục tiêu
    await client.send_message(TARGET_GROUP, modified_message)
    print(f'Gửi tin nhắn: {modified_message}')

async def main():
    await client.start()
    print('Đăng nhập thành công!')

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
