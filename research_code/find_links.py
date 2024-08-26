
def find_links(prompt):
    from setup_gemini import setup_gemini
    gemini = setup_gemini()

    def google_search(query):
        from googlesearch import search
        results = search(query, lang = "en", advanced = True)
        links = [link for link in results]
        return links

    # Search function declaration
    google_search_function_declaration = {
        'name': "google_search",
        'description': "Searches the web and outputs the text of the first 10 links.",
        'parameters': {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query is what you want to search on the web. Make sure to be precise and specific in your query."
                }
            },
            "required": [
                "query"
            ]
        },
    }

    # Gemini queries google and gets the first 10 links
    response = gemini.generate_content(
        prompt,
        tools = [{
            'function_declarations' : [google_search_function_declaration]
        }]
    )
    print(response)
    # Outputs the results of the search function call (with the links)
    function_call = response.candidates[0].content.parts[0].function_call
    args = function_call.args
    if function_call.name == "google_search":
        results = google_search(args["query"])
        useful_links = gemini.generate_content(
            f"Which of the following links are most useful in obtaining information
            that answers the following: {prompt}? Consider the validity of the sources,
            with the UN, international politics research organization (such as the Council 
            Foriegn Relations), educational institutions, and credible news outlets 
            being the most reliable. Also, note that statements by world leaders and 
            national government resources (such as policy plans) are good sources for information
            on that SPECFIC country. These are the links: {results}. Output your results in
            the format of a EXACT python list. DO NOT write ANYTHING ELSE.
            "
        )
        return useful_links





    else:
        return "An error occured. Please try again."
