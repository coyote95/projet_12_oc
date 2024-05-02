from rich.console import Console


class BaseView:
    @staticmethod
    def display_error_message(message):
        console = Console()
        console.print(f'[bold red]ERROR[/bold red]:{message}')

    @staticmethod
    def display_warning_message(message):
        console = Console()
        console.print(f'[bold yellow]WARNING[/bold yellow]:{message}')

    @staticmethod
    def display_info_message(message):
        console = Console()
        console.print(f'[bold blue]INFO[/bold blue]:{message}')
