from telethon import TelegramClient, events

# Thay thế giá trị dưới đây bằng thông tin của bạn
API_ID = '21357718'
API_HASH = 'df3564e279df7787a6292c45b177524a'
PHONE_NUMBER = '+84367729142'

# Khởi tạo client
client = TelegramClient('session_name', API_ID, API_HASH)

# Nhóm nguồn và nhóm đích
source_group = 't.me/thutele1234'
destination_group = 't.me/thutele12344'

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    message = event.message
    # Gửi tin nhắn đến nhóm đích
    await client.send_message(destination_group, message.text)

async def main():
    await client.start()
    print("Đã đăng nhập thành công")

    # Bắt đầu lắng nghe các tin nhắn mới
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
