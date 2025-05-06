from serpapi import GoogleSearch
import os

class WebSearchTool:
    def __init__(self):
        self.api_key = os.getenv('SERPAPI_KEY')

    def run(self, query: str, num_results: int = 3) -> str:
        params = {
            'q': query,
            'engine': 'google',
            'api_key': self.api_key,
            'num': num_results
        }
        search = GoogleSearch(params)
        results = search.get_dict().get('organic_results', [])[:num_results]
        summary = []
        for idx, r in enumerate(results, 1):
            title = r.get('title')
            link = r.get('link')
            summary.append(f"{idx}. {title} - {link}")
        return "\n".join(summary) or "No results found."
