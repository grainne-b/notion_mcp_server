# server.py
import os
from notion_sdk import create_page, get_page_contents, get_specific_page_details, add_content_to_page

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

# Create an MCP server
mcp = FastMCP("Demo")

PARENT_PAGE_ID = "1d21f7216bdb80789f88fccd964b5031"
NOTION_API_KEY = os.getenv("NOTION_API_KEY")

# Add the Notion SDK functions as MCP tools
@mcp.tool()
def create_notion_page(page_name: str):
    """Create a new page in Notion."""
    return create_page(page_name)

@mcp.tool()
def get_notion_page_contents(page_id: str):
    """Get the contents of a Notion page."""
    return get_page_contents(page_id)

@mcp.tool()
def get_notion_page_details(page_id: str):
    """Get specific details of a Notion page."""
    return get_specific_page_details(page_id)

@mcp.tool()
def add_content_to_notion_page(page_id: str, content: str):
    """Add content to a Notion page."""
    return add_content_to_page(page_id, content)

# Existing tools and resources
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]