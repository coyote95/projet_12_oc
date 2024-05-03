from rich.console import Console


class HomeMenuView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        """
        Display the menu options to the user.
        This method iterates through the menu items and prints the available options to the user,
         along with their corresponding keys.
        Returns:
            None
        """
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")

    def get_user_choice(self):
        """
        Get the user's choice from the menu.
        This method displays the menu to the user, prompts them to make a choice,
        and validates the choice.
        Returns:
            callable or None: The selected menu option, which is a callable function,
             or None if the choice is invalid.
        """
        while True:
            self._display_menu()
            choice = input(">> ")
            if choice in self.menu:
                return self.menu[choice]

    @staticmethod
    def display_title(title):
        console = Console()
        console.print(f'[bold magenta]*****   {title}   *****[/bold magenta]')
