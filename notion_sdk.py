import os
from notion_client import Client
from loguru import logger
PARENT_PAGE_ID = "1d21f7216bdb80789f88fccd964b5031"
notion_client = Client(auth=os.getenv("NOTION_API_KEY"))



def create_page(page_name: str):
  logger.info(f"Creating page {page_name}")
  try:
    notion_client.pages.create(
        parent={
            "page_id": PARENT_PAGE_ID
        },
        properties={
            "title": [
                {
                    "text": {
                        "content": page_name
                    }
                }
            ]
        }
    )
    logger.info(f"Page {page_name} created successfully")
  except Exception as e:
    logger.error(f"Error creating page {page_name}: {e}")


def get_page_children(page_id: str):
  logger.info(f"Getting children of page {page_id}")
  try:
    children = notion_client.blocks.children.list(block_id=page_id)
    logger.info(f"Children of page {page_id}: {children}")
  except Exception as e:
    logger.error(f"Error getting children of page {page_id}: {e}")

# Actual usage
# create_page("notion sdk page test!")
# get_page_children(PARENT_PAGE_ID)

