from abc import ABC, abstractmethod

# Abstract Class
class CaffeineBeverage(ABC):
    def prepare_recipe(self):
        """Template method that defines the skeleton of the algorithm."""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print("Boiling water...")

    def pour_in_cup(self):
        print("Pouring into cup...")

    @abstractmethod
    def brew(self):
        """Abstract method that must be implemented by subclasses."""
        pass

    @abstractmethod
    def add_condiments(self):
        """Abstract method that must be implemented by subclasses."""
        pass

    def customer_wants_condiments(self):
        """Hook method that subclasses can override to change behavior."""
        return True  # Default behavior is to add condiments


# Concrete Class: Tea
class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea...")

    def add_condiments(self):
        print("Adding lemon...")


# Concrete Class: Coffee
class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping coffee through filter...")

    def add_condiments(self):
        print("Adding sugar and milk...")

# Modified Coffee Class with User Input for Condiments
class CoffeeWithHook(CaffeineBeverage):
    def brew(self):
        print("Dripping coffee through filter...")

    def add_condiments(self):
        print("Adding sugar and milk...")

    def customer_wants_condiments(self):
        """Override hook to ask the user if they want condiments."""
        answer = input("Would you like sugar and milk in your coffee? (yes/no): ").strip().lower()
        return answer == "yes"


if __name__ == "__main__":
    print("Making tea:")
    tea = Tea()
    tea.prepare_recipe()

    print("\nMaking coffee:")
    coffee = Coffee()
    coffee.prepare_recipe()

    print("\nMaking coffee with user choice:")
    coffee_hook = CoffeeWithHook()
    coffee_hook.prepare_recipe()
