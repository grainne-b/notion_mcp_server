Notion parent page id

```
https://www.notion.so/MCP-Parent-Page-1d21f7216bdb80789f88fccd964b5031
```


Curl example
```
curl --location --request POST 'https://api.notion.com/v1/pages' \
--header 'Authorization: Bearer $NOTION_API_KEY' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-05-13' \
--data '{
"parent": { "page_id": "1d21f7216bdb80789f88fccd964b5031" },
"properties": {
    "title": [
        {
            "text": {
                "content": "Curl example"
            }
        }
    ]
}
}'
```

## Notes
When installing in Claude, the key needs to be hardcoded


## How to run 
```
uv run mcp dev server.py
```

## To use in Claude
```
uv run mcp install server.py
```

Will add to `claude_desktop_config.json`

```
{
  "mcpServers": {
    "Notion MCP Server": {
      "command": "uv",
      "args": [
        "run",
        "mcp",
        "run",
        "/Users/UBHREGR/Documents/repos/experiments/notion_mcp_server/server.py"
      ],
      "env": {
        "NOTION_API_KEY": "REPLACE_ME"
      }
    }
  }
}
```


## Notion package
```
notion-client
```

## Prompt to LLM to create docstrings
```
I am building an MCP (Model Context Protocol) server in Python.
The functions I provide will be registered as tools using @mcp.tool() from FastMCP.

Please generate a concise and informative docstring for each function I give you, following this structure:
	•	A one-line summary describing the function’s purpose.
	•	A section called Args: listing each argument with its type and purpose.
	•	A section called Returns: describing the return value and its type.

The docstring should help both humans and LLMs understand how and when to use the tool.

```