import ollama
from rich.console import Console
from bs4 import BeautifulSoup
import requests

class Summarizer:
    """Responsible for fetching and summarizing article content"""
    def __init__(self, console: Console):
        self.console = console
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def get_article_content(self, url: str) -> str:
        """Fetches and extracts the main content of an article"""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Remove unnecessary elements
            for element in soup.find_all(['script', 'style', 'nav', 'header', 'footer']):
                element.decompose()

            # Extract main content
            content = soup.find('article')
            if content:
                return content.get_text(separator=' ', strip=True)
            return ""
        except Exception as e:
            self.console.print(f"[red]Error fetching content: {str(e)}[/red]")
            return ""

    def summarize(self, content: str) -> str:
        """Generates a summary of the article content using Ollama"""
        try:
            prompt = f"Genera un riassunto semanticamente esaustivo di massimo due paragrafi del seguente testo; il riassunto deve essere in italiano ed avere una lunghezza minima di 100 parole:\n\n{content}"
            response = ollama.chat(model='llama3.2:3b', messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ])
            return response['message']['content']
        except Exception as e:
            self.console.print(f"[red]Error generating summary: {str(e)}[/red]")
            return ""

    def process_article(self, url: str) -> str:
        """Processes an article by fetching its content and generating a summary"""
        content = self.get_article_content(url)
        if not content:
            return "Unable to fetch article content."
        return self.summarize(content)
