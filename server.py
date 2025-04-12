# server.py
import os
import httpx
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

# Create an MCP server
mcp = FastMCP("Demo")


PARENT_PAGE_ID = "1d21f7216bdb80789f88fccd964b5031"
# TODO need to hardcode the key if using it in Claude
NOTION_API_KEY = os.getenv("NOTION_API_KEY")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# @mcp.resource("list_pages://{page_title}")
# def list_pages(page_title: str) -> str:
#     """List all pages in Notion"""
#     return notion_read_page(page_title)

@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

@mcp.tool()
async def notion_add_page(page_title: str) -> str:
    """Create a new page in Notion with the given title. The page_title should be used as input to the api call, in the content body."""
    notion_api_key = os.getenv("NOTION_API_KEY")
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }
    data = {
        "parent": {"page_id": PARENT_PAGE_ID},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": page_title
                        }
                    }
                ]
            }
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.notion.com/v1/pages",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return f"Page '{page_title}' created successfully in Notion."

@mcp.tool()
async def notion_read_page(page_title: str) -> str:
    """Retrieve the contents of a Notion page with the given title."""
    notion_api_key = os.getenv("NOTION_API_KEY")
    headers = {
        "Authorization": f"Bearer {notion_api_key}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }
    # Assuming you have a way to map page_title to page_id
    page_id = PARENT_PAGE_ID
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.notion.com/v1/pages/{page_id}",
            headers=headers
        )
        response.raise_for_status()
        return response.json()


