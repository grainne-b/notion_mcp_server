import os

from loguru import logger
from notion_client import Client

PARENT_PAGE_ID = "1d21f7216bdb80789f88fccd964b5031"
CHILD_PAGE_ID = "1d31f7216bdb81749d50fdee06270fca"
notion_client = Client(auth=os.getenv("NOTION_API_KEY"))


def create_page(page_name: str):
    logger.info(f"Creating page {page_name}")
    try:
        notion_client.pages.create(
            parent={"page_id": PARENT_PAGE_ID},
            properties={"title": [{"text": {"content": page_name}}]},
        )
        logger.info(f"Page {page_name} created successfully")
    except Exception as e:
        logger.error(f"Error creating page {page_name}: {e}")


# Can use this function to get the page ids of the children
# As it will return the page objects, which includes content and child pages
def get_page_contents(page_id: str):
    logger.info(f"Getting children of page {page_id}")
    try:
        children = notion_client.blocks.children.list(block_id=page_id)
        logger.info(f"Children of page {page_id}: {children}")
    except Exception as e:
        logger.error(f"Error getting children of page {page_id}: {e}")


# Unsure how useful this one is
def get_specific_page_details(page_id: str):
    logger.info(f"Getting contents of page {page_id}")
    try:
        page = notion_client.pages.retrieve(page_id=page_id)
        logger.info(f"Contents of page {page_id}: {page}")
    except Exception as e:
        logger.error(f"Error getting contents of page {page_id}: {e}")

def add_content_to_page(page_id: str, content: str):
    logger.info(f"Adding content to page {page_id}")
    try:
        notion_client.blocks.children.append(
    block_id=page_id,
    children=[
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": content
                        }
                    }
                ]
            }
        }
    ]
)
        logger.info(f"Content added to page {page_id} successfully")
    except Exception as e:
        logger.error(f"Error adding content to page {page_id}: {e}")

# Actual usage
# create_page("notion sdk page test!")
# get_page_contents(PARENT_PAGE_ID)
# get_specific_page_details(CHILD_PAGE_ID)

add_content_to_page(CHILD_PAGE_ID, "Adding content from my python script!")
