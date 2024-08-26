from find_links import google_search
from setup_gemini import setup_gemini
from access_web_page_text import access_web_page_text
setup_gemini()

# Search function declaration
google_search_func_declaration = {
    'name': "google_search",
    'description': "Searches the web and outputs the text of the first 10 links.",
    'parameters': {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The query is what you want to search on the web"
            }
        },
        "required": [
            "query"
        ]
    },
}


prompt = "What is the news for today?"
#text = gemini.generate_content(prompt).text
#print(text)

print(google_search(prompt))