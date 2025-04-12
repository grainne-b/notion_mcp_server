import os

from loguru import logger
from notion_client import Client

PARENT_PAGE_ID = "1d21f7216bdb80789f88fccd964b5031"
CHILD_PAGE_ID = "1d31f7216bdb81749d50fdee06270fca"
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
notion_client = Client(auth=os.getenv("NOTION_API_KEY"))


def create_page(page_name: str):
    """
    Create a new page with the specified name in the Notion workspace.

    Args:
        page_name (str): The name of the page to be created.

    Returns:
        True if the page was created successfully, False otherwise. 
    """
    logger.info(f"Creating page {page_name}")
    try:
        notion_client.pages.create(
            parent={"page_id": PARENT_PAGE_ID},
            properties={"title": [{"text": {"content": page_name}}]},
        )
        logger.info(f"Page {page_name} created successfully")
        return True
    except Exception as e:
        logger.error(f"Error creating page {page_name}: {e}")
        return False

def get_page_contents(page_id: str):
    """
    Retrieve and log the children of a specified page in the Notion workspace.

    Args:
        page_id (str): The ID of the page whose children are to be retrieved.

    Returns:
        list: A list of children blocks of the specified page.
    """
    logger.info(f"Getting children of page {page_id}")
    try:
        children = notion_client.blocks.children.list(block_id=page_id)
        logger.info(f"Children of page {page_id}: {children}")
        return children
    except Exception as e:
        logger.error(f"Error getting children of page {page_id}: {e}")


# Unsure how useful this one is
def get_specific_page_details(page_id: str):
    """
    Retrieve and log the details of a specific page in the Notion workspace.

    Args:
        page_id (str): The ID of the page to retrieve details for.

    Returns:
        dict: A dictionary containing the details of the specified page.
    """
    logger.info(f"Getting contents of page {page_id}")
    try:
        page = notion_client.pages.retrieve(page_id=page_id)
        logger.info(f"Contents of page {page_id}: {page}")
        return page
    except Exception as e:
        logger.error(f"Error getting contents of page {page_id}: {e}")

def add_content_to_page(page_id: str, content: str):
    """
    Add specified content to a page in the Notion workspace.

    Args:
        page_id (str): The ID of the page to which content will be added.
        content (str): The content to be added to the page.

    Returns:
        None
    """
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

# add_content_to_page(CHILD_PAGE_ID, "Adding content from my python script!")
