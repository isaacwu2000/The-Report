import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
gemini =  genai.GenerativeModel("gemini-1.5-flash")

def google_search(query):
    from googlesearch import search
    results = search(query, lang = "en", advanced = True)
    for i in results:
        print(i, "\n")

# Search function declaration
"""
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
"""

prompt = "What is the news for today?"
#text = gemini.generate_content(prompt).text
#print(text)

google_search("Who is the Gegi guy?")