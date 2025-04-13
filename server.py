# server.py
import os
import sys
from loguru import logger
from notion_sdk import create_page, get_page_contents, get_specific_page_details, add_content_to_page

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base


logger.remove()
# Add a new logger configuration that outputs to stderr
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


# Create an MCP server
mcp = FastMCP("Notion MCP Server")

PARENT_PAGE_ID = "1d21f7216bdb80789f88fccd964b5031"
NOTION_API_KEY = os.getenv("NOTION_API_KEY")


# # Add the Notion SDK functions as MCP tools
mcp.tool()(create_page)
mcp.tool()(get_page_contents)
mcp.tool()(get_specific_page_details)
mcp.tool()(add_content_to_page)

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


logger.info("✅ LOGURU LINE MCP server loaded and ready (waiting on MCP runtime to serve)")
print("✅ MCP server loaded and ready (waiting on MCP runtime to serve)")
