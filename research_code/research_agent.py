from find_links import find_links
from access_web_page_text import access_web_page_text
from setup_gemini import setup_gemini
gemini = setup_gemini()

goal = "create a topic overview of the russo-ukrainian war"
# Findig relavant links for the user's desired result
relevant_links = (
    find_links(f"""
        Perform a Google Search to find relevant and credible 
        resources that help {goal}.
        """)   
)


# Getting the text from each page for the topic overview
research_text = []
for link in relevant_links:
    unclean_page_text = access_web_page_text(link)
    clean_page_text = gemini.generate_content(f"""
        Clean up unnesesary elements in the following text
        and convert it to a high-quality plain text format (not markdown). Remove unncessary spaces and 
        information that is unrelated in any way or form with the this task:
        {goal}. Here is the text to clean: {unclean_page_text}.
        """).text
    research_text.append({"url":link, "text":clean_page_text})
    print(research_text)
print(research_text)
