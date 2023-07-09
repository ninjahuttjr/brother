get_current_datetime_func = {
    "name": "get_current_datetime",
    "description": "Returns the current date and time",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

browse_web_func = {
    "name": "browse_web",
    "description": "Fetches the content of a webpage",
    "parameters": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The URL of the webpage to browse"
            }
        },
        "required": ["url"]
    }
}

search_gif_func = {
    "name": "search_gif",
    "description": "Searches for a GIF using the GIPHY API",
    "parameters": {
        "type": "object",
        "properties": {
            "search_term": {
                "type": "string",
                "description": "The term to search for"
            }
        },
        "required": ["search_term"]
    }
}
