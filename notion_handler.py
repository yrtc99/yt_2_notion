from notion_client import Client
from config import NOTION_TOKEN, NOTION_DATABASE_ID

notion = Client(auth=NOTION_TOKEN)

def create_notion_page(text, vid_name, llama_summary):
    #創建page屬性(結構)，讓notion知道這個page是什麼，我要建立的page會繼承這個結構
    page_properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": vid_name
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

    # 創建page，結構是page_properties
    new_page = notion.pages.create(
        parent={"database_id": NOTION_DATABASE_ID},
        properties=page_properties
    )
    
    # notion有限制2000字，所以需要分割transcription text
    def chunk_text(text, chunk_size=2000):
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    text_chunks = chunk_text(text)

    # 將text_chunks分割成多個blocks，blocks裡面就是chunk(文字內容)
    # blocks = [] #這是沒有分段的block設計
    
    # 摘要的段落blocks設計
    blocks = [
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "摘要"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": llama_summary}}]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "Whole Speech Transcription"}}]
            }
        }
    ]
    
    text_chunks = chunk_text(text)
    for chunk in text_chunks:
        blocks.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{
                    "type": "text", 
                    "text": {"content": chunk}
                    }]
            }
        })


    # 更新页面内容，将所有blocks一次加到page里
    notion.blocks.children.append(
        block_id=new_page["id"],
        children=blocks  # 直接使用blocks列表
    )
    return new_page