from bs4 import BeautifulSoup
from typing import List
from .models import Article

class NewsParser:
    """Responsible for parsing news articles from the webpage"""
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    def get_news(self) -> List[Article]:
        """Retrieves the last 5 news from Il Post"""
        if not self.soup:
            return []

        news_items = []
        articles = self.soup.find_all('article')[:5]

        for article in articles:
            if article.find('a'):
                title = article.find('a').text.strip()
                link = article.find('a')['href']
                date_elem = article.find('time')
                date = date_elem.text.strip() if date_elem else "Date not available"

                news_items.append(Article(
                    title=title,
                    link=link,
                    date=date
                ))

        return news_items

    def get_main_content_articles(self) -> List[Article]:
        """Retrieves the last 5 articles from the main content section"""
        if not self.soup:
            return []

        articles = []
        article_elements = self.soup.select('#main-content > div > div > article')[:5]

        for article in article_elements:
            if article.find('a'):
                if article.find('h2'):
                    title = article.find('h2').text.strip()
                else:
                    title = article.find('a').text.strip()
                link = article.find('a')['href']

                articles.append(Article(
                    title=title,
                    link=link
                ))

        return articles
