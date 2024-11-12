from abc import ABC, abstractmethod


# Component Interface
class Beverage(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


# Concrete Component: Espresso
class Espresso(Beverage):
    def cost(self):
        return 1.99

    def description(self):
        return "Espresso"


# Concrete Component: HouseBlend
class HouseBlend(Beverage):
    def cost(self):
        return 0.89

    def description(self):
        return "House Blend Coffee"


# Decorator Base Class
class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage


# Concrete Decorator: Milk
class Milk(CondimentDecorator):
    def cost(self):
        return self.beverage.cost() + 0.10

    def description(self):
        return self.beverage.description() + ", Milk"


# Concrete Decorator: Mocha
class Mocha(CondimentDecorator):
    def cost(self):
        return self.beverage.cost() + 0.20

    def description(self):
        return self.beverage.description() + ", Mocha"


# Concrete Decorator: Soy
class Soy(CondimentDecorator):
    def cost(self):
        return self.beverage.cost() + 0.15

    def description(self):
        return self.beverage.description() + ", Soy"


if __name__ == "__main__":
    # Create an Espresso
    beverage = Espresso()
    print(f"{beverage.description()} ${beverage.cost()}")

    # Add Mocha to the Espresso
    beverage = Mocha(beverage)
    print(f"{beverage.description()} ${beverage.cost()}")

    # Add another Mocha
    beverage = Mocha(beverage)
    print(f"{beverage.description()} ${beverage.cost()}")

    # Add Soy
    beverage = Soy(beverage)
    print(f"{beverage.description()} ${beverage.cost()}")
