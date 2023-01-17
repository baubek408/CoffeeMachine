class MenuItems:
    """Models each menu items."""
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItems(name='latte', cost=2.5, water=200, milk=150, coffee=24),
            MenuItems(name='espresso', cost=1.5, water=50, milk=0, coffee=18),
            MenuItems(name='cappuccino', cost=3, water=250, milk=50, coffee=24),
        ]

    def get_items(self):
        """Returns all the names of available menu items."""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drinks(self, order_name):
        """Searches the menu for particular drink by name. Returns that item if it exists, otherwise returns None."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
