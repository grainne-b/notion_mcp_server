## Setting Up Notion API Key and Permissions

### Creating a Notion API Key

1. **Go to Notion Integrations:**
   - Visit [Notion Integrations](https://www.notion.so/my-integrations) and log in with your Notion account.

2. **Create a New Integration:**
   - Click on "New Integration" and fill out the required fields such as the name of the integration, and select the workspace you want to connect to.

3. **Save the Integration:**
   - After filling out the details, click "Submit" to create the integration. You will be provided with an API key.

4. **Copy the API Key:**
   - Copy the API key and store it securely. You will use this key to authenticate your requests to the Notion API.

### Giving a Page Permissions to Use the Integration

1. **Open Notion:**
   - Navigate to the page you want to give permissions to.

2. **Share the Page:**
   - Click on the "Share" button at the top right of the page.

3. **Invite the Integration:**
   - In the "Invite" field, type the name of your integration and select it from the dropdown. This will give the integration access to the page.

4. **Set Permissions:**
   - Ensure the integration has the necessary permissions (e.g., read, write) to perform the actions you need.

### Code update
In `notion_sdk.py` , update the PAGE_ID, with the PAGE_ID of the page you created above.
The page id can be retrieved by copying the page link



### Setting Up `uv` for Python

1. **Install `uv` using Homebrew:**
   - Ensure you have Homebrew installed on your system.
   - Run the following command to install `uv`:
     ```bash
     brew install uv
     ```

2. **Verify Installation:**
   - Check if `uv` is installed correctly by running:
     ```bash
     uv --version
     ```

3. **Basic Usage:**
   - You can run a Python script using `uv` with:
     ```bash
     uv run <your_script.py>
     ```



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


```
{
  "mcpServers": {
    "Notion MCP Server": {
"command": "bash",
"args": [
  "-c",
  "source /Users/UBHREGR/Documents/repos/experiments/notion_mcp_server/.venv/bin/activate && uv run mcp run /Users/UBHREGR/Documents/repos/experiments/notion_mcp_server/server.py"
      ],
      "env": {
        "NOTION_API_KEY": "TODO"
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