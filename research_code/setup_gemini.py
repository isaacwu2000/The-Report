def setup_gemini(): 
    import os
    from dotenv import load_dotenv
    import google.generativeai as genai

    load_dotenv()
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    return genai.GenerativeModel("gemini-1.5-flash")