def access_web_page_text(url):
    import requests
    from bs4 import BeautifulSoup

    web_page = requests.get(url)
    web_page_text = BeautifulSoup(web_page.content, 'html.parser').get_text()
    return str(web_page_text)

