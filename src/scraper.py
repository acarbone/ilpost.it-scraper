from rich.console import Console
from .fetcher import PageFetcher
from .parser import NewsParser
from .display import NewsDisplay
from .browser import NewsBrowser

class IlPostScraper:
    """Main class coordinating the scraping process"""
    def __init__(self):
        self.console = Console()
        self.fetcher = PageFetcher()
        self.display = NewsDisplay(self.console)
        self.browser = NewsBrowser(self.console)

    def run(self):
        """Main execution method"""
        # Fetch the page
        soup = self.fetcher.fetch()
        if not soup:
            return

        # Parse and display news
        parser = NewsParser(soup)
        news_items = parser.get_news()
        if news_items:
            self.display.display_news(news_items, "Last 5 news from Il Post", True, start_index=1)
            self.console.print("\n")

        # Parse and display main content articles
        main_articles = parser.get_main_content_articles()
        if main_articles:
            self.display.display_news(main_articles, "Last 5 articles from Il Post", start_index=len(news_items) + 1)

            # Combine both lists for link opening
            all_items = news_items + main_articles

        # Handle user interaction
        while self.browser.handle_user_input(all_items):
            pass
