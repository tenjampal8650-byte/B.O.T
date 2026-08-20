import webbrowser
from urllib.parse import quote


class WebSearchSkill:

    name = "web_search"

    description = "Searches the web using the default browser."

    def execute(self, query):
        query = query.strip()

        if not query:
            return "What should I search for?"

        url = "https://www.google.com/search?q=" + quote(query)

        webbrowser.open(url)

        return f"Searching the web for: {query}"