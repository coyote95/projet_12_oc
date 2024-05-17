class MenuEntry:
    """
    Represents a menu entry or option with an associated handler function.
    Attributes:
    - option: A string representing the menu option.
    - handler: A function that will be called when this menu option is selected.
    """

    def __init__(self, option, handler):
        self.option = option
        self.handler = handler

    def __repr__(self):
        return f"MenuEntry: {self.option}, {self.handler})"

    def __str__(self):
        return str(self.option)


class Menu:
    """
    Represents a menu that can store and manage menu entries with associated handlers.
    Attributes:
    - _entries: A dictionary that stores menu entries where keys are identifiers and values are MenuEntry objects.
    - _autokey: An internal counter used to automatically generate unique identifiers for menu entries.
    Example usage:
    my_menu = Menu()
    my_menu.add("1", "Option 1", some_function)
    """

    def __init__(self):
        self._entries = {}
        self._autokey = 1

    def add(self, key, option, handler):
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1
        self._entries[str(key)] = MenuEntry(option, handler)

    def items(self):
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]
