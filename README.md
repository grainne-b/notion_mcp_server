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