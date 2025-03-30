from typing import List
import webbrowser
from rich.console import Console
from .models import Article

class NewsBrowser:
    """Responsible for handling user interaction and opening articles"""
    def __init__(self, console: Console):
        self.console = console

    def open_article(self, articles: List[Article], index: int) -> None:
        """Opens an article in the default browser"""
        if 0 <= index < len(articles):
            webbrowser.open(articles[index].link)
        else:
            self.console.print("[red]Invalid number. Please try again.[/red]")

    def handle_user_input(self, all_items: List[Article]) -> bool:
        """Handles user input and returns False if user wants to quit"""
        try:
            choice = self.console.input("\n[bold green]Enter the number of the article to open (or 'q' to quit): [/bold green]")
            if choice.lower() == 'q':
                return False

            idx = int(choice) - 1
            self.open_article(all_items, idx)
            return True
        except ValueError:
            self.console.print("[red]Please enter a valid number.[/red]")
            return True
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")
            return True
