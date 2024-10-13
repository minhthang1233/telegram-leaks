from telethon import TelegramClient

# Thông tin đăng nhập tài khoản người dùng
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    # Lấy tin nhắn từ nhóm nguồn
    async for message in client.iter_messages('group_source_username', limit=10):
        if message.text:
            print(f"Original message: {message.text}")
            modified_message = modify_links(message.text)
            print(f"Modified message: {modified_message}")

            # Gửi tin nhắn đã sửa sang nhóm đích
            await client.send_message('group_target_username', modified_message)

# Hàm này sẽ sửa các liên kết trong bài viết
def modify_links(text):
    # Ví dụ: thay thế tất cả các link 'lazada.com' thành 'example.com'
    modified_text = text.replace('lazada.com', 'example.com')
    return modified_text

with client:
    client.loop.run_until_complete(main())
