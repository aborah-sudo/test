from abc import ABC, abstractmethod

class MenuComponent(ABC):
    """Abstract base class for menu components"""
    def add(self, component):
        raise NotImplementedError()

    def remove(self, component):
        raise NotImplementedError()

    def display(self):
        raise NotImplementedError()

class MenuItem(MenuComponent):
    """Represents an individual menu item"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name}: ${self.price:.2f}")

class CompositeMenu(MenuComponent):
    """Represents a menu that can contain other menus or menu items"""
    def __init__(self, name):
        self.name = name
        self.menu_components = []

    def add(self, component):
        self.menu_components.append(component)

    def remove(self, component):
        self.menu_components.remove(component)

    def display(self):
        print(f"\n{self.name} Menu:")
        print("-" * len(f"{self.name} Menu:"))
        for component in self.menu_components:
            component.display()

if __name__ == "__main__":
    # Create menu items
    pasta = MenuItem("Pasta", 12.99)
    pizza = MenuItem("Pizza", 10.99)
    salad = MenuItem("Salad", 7.99)
    coffee = MenuItem("Coffee", 2.99)
    tea = MenuItem("Tea", 1.99)

    # Create menus
    dinner_menu = CompositeMenu("Dinner")
    drinks_menu = CompositeMenu("Drinks")

    # Add items to menus
    dinner_menu.add(pasta)
    dinner_menu.add(pizza)
    dinner_menu.add(salad)

    drinks_menu.add(coffee)
    drinks_menu.add(tea)

    # Create the main menu and add submenus
    main_menu = CompositeMenu("Main")
    main_menu.add(dinner_menu)
    main_menu.add(drinks_menu)

    # Display the entire menu hierarchy
    main_menu.display()

