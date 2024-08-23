import streamlit as st
import os
from config import YOUTUBE_DOWNLOAD_PATH
from youtube_handler import download_youtube_audio
from whisper_handler import transcribe_audio
from notion_handler import create_notion_page
from llama_handler import generate_summary

st.set_page_config(page_title="YouTube to Notion Transcription", page_icon="🎥")

def add_bg_from_css():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(to right top, #d16ba5, #c777b9, #ba83ca, #aa8fd8, #9a9ae1, #8aa7ec, #79b3f4, #69bff8, #52cffe, #41dfff, #46eefa, #5ffbf1);
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    # add_bg_from_css() 
    st.title('YouTube to Notion Transcription')

    url = st.text_input('Enter YouTube URL:')
    if st.button('Process'):
        if url:
            with st.spinner('Processing...'):
                try:
                    # 下載音頻
                    audio_file, file_name = download_youtube_audio(url)  # in youtube_handler.py
                    st.success(f"Audio downloaded: {audio_file}")

                    # 轉錄音頻
                    transcription = transcribe_audio(audio_file)  # in whisper_handler.py
                    st.success("Audio transcribed successfully")
                    st.subheader("Transcription:")
                    st.write(transcription)
                    
                    # 生成摘要
                    summary = generate_summary(transcription)
                    st.subheader("summary:")
                    st.write("原始摘要输出：", repr(summary))
                    # st.write(summary)
                    
                    # 創建Notion頁面
                    new_page = create_notion_page(transcription, file_name, summary)  # in notion_handler.py
                    st.success(f"Transcription added to Notion successfully! Page ID: {new_page['id']}")

                    # 清理臨時文件
                    os.remove(audio_file)
                except Exception as e:
                    st.error(f'An error occurred: {str(e)}')
        else:
            st.warning("Please enter a YouTube URL")

if __name__ == "__main__":
    main()
    