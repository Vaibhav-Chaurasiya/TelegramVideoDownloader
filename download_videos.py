from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaDocument
import os
from dotenv import load_dotenv

# ✅ Load from .env file
load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
save_path = os.getenv("SAVE_PATH", "videos")
session_name = 'course_downloader'

if not os.path.exists(save_path):
    os.makedirs(save_path)

client = TelegramClient(session_name, api_id, api_hash)

with client:
    print("\n📋 Select a chat/group/channel to download videos from:\n")
    dialogs = list(client.iter_dialogs())
    for i, dialog in enumerate(dialogs):
        print(f"{i + 1}. {dialog.name}")

    while True:
        try:
            choice = int(input("\n👉 Enter the number of the chat to download from: ")) - 1
            if 0 <= choice < len(dialogs):
                break
            else:
                print("❌ Invalid choice! Please select from the list.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    target_chat = dialogs[choice].id
    chat_name = dialogs[choice].name

    print(f"\n📥 Scanning '{chat_name}' for video messages...\n")

    all_messages = []
    for msg in client.iter_messages(target_chat):
        if msg.video:
            all_messages.append(msg)

    total = len(all_messages)
    print(f"🔍 Found {total} video(s) in '{chat_name}'. Starting download...\n")

    count = 0
    for idx, message in enumerate(reversed(all_messages), 1):
        media_name = message.file.name if message.file else f"{message.id}.mp4"
        full_path = os.path.join(save_path, media_name)

        if os.path.exists(full_path):
            print(f"[{idx}/{total}] ⏩ Skipped (already exists): {media_name}")
            continue

        try:
            filename = client.download_media(message, file=save_path)
            count += 1
            print(f"[{idx}/{total}] ✅ Downloaded: {filename}")
        except Exception as e:
            print(f"[{idx}/{total}] ❌ Failed: {e}")

    print(f"\n🎉 Done! {count} new video(s) downloaded. Skipped {total - count}.\n")
