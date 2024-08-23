import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
YOUTUBE_DOWNLOAD_PATH = "downloaded_audio"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not os.path.exists(YOUTUBE_DOWNLOAD_PATH):
    os.makedirs(YOUTUBE_DOWNLOAD_PATH)