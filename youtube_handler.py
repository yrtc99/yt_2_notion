import yt_dlp as youtube_dl
import os
from config import YOUTUBE_DOWNLOAD_PATH

def download_youtube_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(YOUTUBE_DOWNLOAD_PATH, '%(title)s.%(ext)s'),
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        audio_file = ydl.prepare_filename(info_dict)
        to_transcript_file = os.path.splitext(audio_file)[0] + '.wav'
        file_name = os.path.basename(to_transcript_file)
        return to_transcript_file, file_name  # 為了傳值file_name到notion_handler.py
    