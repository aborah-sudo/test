from abc import ABC, abstractmethod

class Iterator(ABC):
    """Abstract Iterator Interface"""
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class MenuIterator(Iterator):
    """Iterator for menu items"""
    def __init__(self, items):
        self.items = items
        self.position = 0

    def has_next(self):
        return self.position < len(self.items)

    def next(self):
        if not self.has_next():
            raise StopIteration
        item = self.items[self.position]
        self.position += 1
        return item

class IterableCollection(ABC):
    """Abstract Collection Interface"""
    @abstractmethod
    def create_iterator(self):
        pass

class Menu(IterableCollection):
    """A collection of menu items"""
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def create_iterator(self):
        return MenuIterator(self.menu_items)

if __name__ == "__main__":
    # Create a menu and add items
    menu = Menu()
    menu.add_item("Pasta")
    menu.add_item("Pizza")
    menu.add_item("Salad")

    # Get the iterator
    iterator = menu.create_iterator()

    # Iterate through the menu
    print("Menu Items:")
    while iterator.has_next():
        print(iterator.next())
