from telethon import TelegramClient

# Thông tin đăng nhập tài khoản người dùng
api_id = '21357718'     # Thay thế YOUR_API_ID bằng API ID của bạn
api_hash = 'df3564e279df7787a6292c45b177524a' # Thay thế YOUR_API_HASH bằng API Hash của bạn
phone_number = '+84367729142' # Thay thế YOUR_PHONE_NUMBER bằng số điện thoại của bạn

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    # Thay thế 'sanbanshopee' bằng username của nhóm nguồn
    async for message in client.iter_messages('sanbanshopee', limit=10):
        if message.text:
            print(f"Original message: {message.text}")
            modified_message = modify_links(message.text)
            print(f"Modified message: {modified_message}")

            # Thay thế 'thutele12344' bằng username của nhóm đích
            await client.send_message('thutele12344', modified_message)

# Hàm này sẽ sửa các liên kết trong bài viết
def modify_links(text):
    # Ví dụ: thay thế tất cả các link 'lazada.com' thành 'example.com'
    modified_text = text.replace('lazada.com', 'example.com')
    return modified_text

with client:
    client.loop.run_until_complete(main())
