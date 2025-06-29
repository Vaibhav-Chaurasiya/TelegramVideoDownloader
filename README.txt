# Telegram Video Downloader 📥

Python script using [Telethon](https://github.com/LonamiWebs/Telethon) to download all videos from any Telegram group, channel, or private chat.

## 🔧 Features
- Chat/channel selector
- Smart resume (skips already downloaded videos)
- Progress status for each video
- Auto folder creation

## 🚀 Setup

1. Go to https://my.telegram.org to get your `api_id` and `api_hash`
2. Edit `download_videos.py` and update:
   - `api_id`
   - `api_hash`
   - `save_path`

3. Install dependencies:
```bash
pip install -r requirements.txt
