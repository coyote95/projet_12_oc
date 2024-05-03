from rich.console import Console


class BaseView:
    @staticmethod
    def display_error_message(message):
        console = Console()
        console.print(f'[bold red]ERROR: {message}[/bold red]')

    @staticmethod
    def display_warning_message(message):
        console = Console()
        console.print(f'[bold yellow]WARNING: {message}[/bold yellow]')

    @staticmethod
    def display_info_message(message):
        console = Console()
        console.print(f'[bold green]INFO: {message}[/bold green]')
