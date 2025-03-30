from typing import List
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from .models import Article

class NewsDisplay:
    """Responsible for displaying news in a formatted way"""
    def __init__(self, console: Console):
        self.console = console

    def display_news(self, news_items: List[Article], title: str = "Last 5 news from Il Post",
                    has_date: bool = False, start_index: int = 1) -> None:
        """Displays the news in a formatted table"""
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("№", style="dim")
        table.add_column("Title")
        if has_date:
            table.add_column("Time")

        for idx, item in enumerate(news_items, start_index):
            title_text = Text(item.title)
            title_text.stylize(f"link {item.link}")
            if has_date:
                table.add_row(str(idx), title_text, item.date)
            else:
                table.add_row(str(idx), title_text)

        self.console.print(Panel(table, title=f"[bold blue]{title}[/bold blue]"))
