def google_search(query):
    from googlesearch import search
    results = search(query, lang = "en", advanced = True)
    links = [link for link in results]
    return links