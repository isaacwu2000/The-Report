from find_links import find_links
from access_web_page_text import access_web_page_text
from setup_gemini import setup_gemini
gemini = set_up_gemini()

print(find_links("Perform a Google Search giving an overview of the Russo-Ukrainian War and the key countries involved:"))

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
# Find rel