import requests
from bs4 import BeautifulSoup
from typing import Optional
from rich.console import Console

class PageFetcher:
    """Responsible for fetching and parsing the webpage"""
    def __init__(self):
        self.url = "https://www.ilpost.it"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.console = Console()

    def fetch(self) -> Optional[BeautifulSoup]:
        """Fetches the webpage and returns a BeautifulSoup object"""
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            self.console.print(f"[red]Error fetching page: {str(e)}[/red]")
            return None
