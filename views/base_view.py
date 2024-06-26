from rich.console import Console

"""
Provides methods to display messages in different colors using the Rich library.

Methods:
    display_error_message(message): Displays an error message in bold red color.
    display_warning_message(message): Displays a warning message in bold yellow color.
    display_info_message(message): Displays an info message in bold green color.
"""


class BaseView:
    @staticmethod
    def display_error_message(message):
        console = Console()
        console.print(f"[bold red]ERROR: {message}[/bold red]")

    @staticmethod
    def display_warning_message(message):
        console = Console()
        console.print(f"[bold yellow]WARNING: {message}[/bold yellow]")

    @staticmethod
    def display_info_message(message):
        console = Console()
        console.print(f"[bold green]INFO: {message}[/bold green]")
