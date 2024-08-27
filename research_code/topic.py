from find_links import find_links
from access_web_page_text import access_web_page_text
from setup_gemini import setup_gemini
import ast

gemini = setup_gemini()

topic = "Russo-Ukrainian War"

"""
Topic Research Prompt:
1) Get an overview of the issue and the key-players/countries involved
    a) Explain the positions of these key-players and the sides/perseptives of the issue
2) Precisely identify the issue
    a) How and why it occured
    b) The consequences of inaction
3) Break down the issue and figure out each of its parts and how they connect to the bigger issue
4) Explain some of the current events on the topic (focus on the most important and relevant parts)
5) Explain major past international actions such as UN resolutions & conventions as well as Treaties between nations
6) Record other important information and key statistics
"""
# Finding relevant links to make a topic overview
topic_overview_links = ast.literal_eval(find_links(f"Perform a Google Search to find relevant and credible links that give an overview of the {topic} and the key-players/countries involved."))
print(topic_overview_links)
# Getting the text from each page for the topic overview
topic_overview_pages = []
for link in topic_overview_links:
    topic_overview_pages.append({"url":link, "text":access_web_page_text(link)})

print(topic_overview_pages)