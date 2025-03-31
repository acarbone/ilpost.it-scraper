from typing import List
import webbrowser
from rich.console import Console
from rich.panel import Panel
from .models import Article
from .summarizer import Summarizer

class NewsBrowser:
    """Responsible for handling user interaction and opening articles"""
    def __init__(self, console: Console):
        self.console = console
        self.summarizer = Summarizer(console)

    def open_article(self, articles: List[Article], index: int) -> None:
        """Opens an article in the default browser"""
        if 0 <= index < len(articles):
            webbrowser.open(articles[index].link)
        else:
            self.console.print("[red]Invalid number. Please try again.[/red]")

    def summarize_article(self, articles: List[Article], index: int) -> None:
        """Summarizes an article using Ollama"""
        if 0 <= index < len(articles):
            article = articles[index]
            self.console.print(f"\n[bold blue]Generating summary for: {article.title}[/bold blue]")
            summary = self.summarizer.process_article(article.link)
            if summary:
                self.console.print(Panel(summary, title="[bold green]Summary[/bold green]"))
        else:
            self.console.print("[red]Invalid number. Please try again.[/red]")

    def handle_user_input(self, all_items: List[Article]) -> bool:
        """Handles user input and returns False if user wants to quit"""
        try:
            choice = self.console.input("\n[bold green]Enter article number to open, 's:number' for summary (or 'q' to quit): [/bold green]")
            if choice.lower() == 'q':
                return False

            if choice.startswith('s:'):
                try:
                    idx = int(choice[2:]) - 1
                    self.summarize_article(all_items, idx)
                except ValueError:
                    self.console.print("[red]Please enter a valid number after 's:'.[/red]")
            else:
                idx = int(choice) - 1
                self.open_article(all_items, idx)
            return True
        except ValueError:
            self.console.print("[red]Please enter a valid number.[/red]")
            return True
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")
            return True
