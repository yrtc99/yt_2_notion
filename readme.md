# YouTube to Notion Tool

This tool converts YouTube videos into text using Whisper for speech-to-text and extracts summaries with Llama, automatically saving the results to a Notion database.
[demo video](https://youtu.be/4gRKq7Wg6Mg)

## Project Structure

```
/home/n56101903/STTnotion
|-- __pycache__
|   |-- config.cpython-38.pyc
|   |-- notion_handler.cpython-38.pyc
|   |-- whisper_handler.cpython-38.pyc
|   `-- youtube_handler.cpython-38.pyc
|-- config.py
|-- downloaded_audio
|   `-- yt_vid_you_download.wav
|-- main.py
|-- notion_handler.py
|-- requirements.txt
|-- whisper_handler.py
`-- youtube_handler.py

```

## Requirements

To run this tool, you need to:

1. Install the necessary libraries: `streamlit`, `youtube_dl`, `whisper`, `notion-client`
2. Obtain a Notion API key and database ID
3. Install FFmpeg (for audio processing)

### Setting Up the Environment

Create a `.env` file to store your Notion API key and database ID:

```
NOTION_TOKEN=your_notion_api_key_here
NOTION_DATABASE_ID=your_notion_database_id_here

```

## Running the Program

1. Install the required libraries:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
2. Ensure you have FFmpeg installed.
3. Set up your `.env` file with the Notion API key and database ID.
4. Run the program:
    
    ```bash
    streamlit run main.py
    
    ```
    

## Troubleshooting

### FFmpeg Installation

To check if FFmpeg is installed, open your command line (terminal) and type:

```bash
ffmpeg -version

```

If FFmpeg is installed, you will see version information. If not, you’ll receive an error message.

- **Installing FFmpeg**:
    - **Windows**:
        - Use Chocolatey (package manager):
            
            ```bash
            choco install ffmpeg
            
            ```
            
        - Or download from the [official website](https://ffmpeg.org/download.html).
    - **macOS**:
        - Use Homebrew:
            
            ```bash
            brew install ffmpeg
            
            ```
            
    - **Linux (Ubuntu/Debian)**:
        
        ```bash
        sudo apt update
        sudo apt install ffmpeg
        
        ```
        

After installation, run `ffmpeg -version` again to confirm success.

### YouTube-DL Issues

If you encounter an error such as `Unable to extract uploader id`, you may need to update `yt-dlp`:

```bash
python3 -m pip install --force-reinstall <https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz>

```

Then, run:

```bash
yt-dlp URL

```

Ensure you import it correctly in your project:

```python
import yt_dlp as youtube_dl

```

### Notion API Setup

1. Create a Notion integration to obtain the API key.
    ![image](https://github.com/user-attachments/assets/84ae1650-4f7b-4574-89b6-74e9140e9b26)
    
    
2. Add the integration to your Notion database to retrieve the database ID.
    ![image1](https://github.com/user-attachments/assets/b42abdf2-0449-433e-b49b-c5a31fd28520)

    
3. To find your Notion database ID, locate the URL of your database:
    
    `https://www.notion.so/<long_hash_1>?v=<long_hash_2>`
    
    `<long_hash_1>` is your database ID.
    

### Property Settings in Notion

If you encounter errors such as “Title is not a property that exists” or “Content is not a property that exists”, ensure the properties are correctly defined in your Notion database. Update the `notion_handler.py` with the correct property names:
![image2](https://github.com/user-attachments/assets/1899b0b8-e59a-4c48-a632-5b369fb415f9)


Original Code:

```python
def create_notion_page(text):
    new_page = notion.pages.create(
        parent={"database_id": NOTION_DATABASE_ID},
        properties={
            "Title": {"title": [{"text": {"content": "YouTube Transcription"}}]},
            "Content": {"rich_text": [{"text": {"content": text[:2000]}}]},  # Notion API limit
        },
    )

```

Updated Code:

```python
page_properties = {
    "Name": {
        "title": [
            {
                "text": {
                    "content": file_name
                }
            }
        ]
    },
    "Tags": {
        "multi_select": [
            {"name": "content"}
        ]
    }
}
new_page = notion.pages.create(
    parent={"database_id": NOTION_DATABASE_ID},
    properties=page_properties
)

```

---

This refined version includes clear instructions, troubleshooting tips, and code examples that will help users understand and effectively use your tool.
