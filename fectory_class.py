
from abc import ABC, abstractmethod

# Abstract Pizza Class


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass


# Concrete Pizza: Cheese Pizza
class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing Cheese Pizza...")

    def bake(self):
        print("Baking Cheese Pizza...")

    def cut(self):
        print("Cutting Cheese Pizza...")

    def box(self):
        print("Boxing Cheese Pizza...")


# Concrete Pizza: Pepperoni Pizza
class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza...")

    def bake(self):
        print("Baking Pepperoni Pizza...")

    def cut(self):
        print("Cutting Pepperoni Pizza...")

    def box(self):
        print("Boxing Pepperoni Pizza...")


# Pizza Factory
class SimplePizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")


# Pizza Store
class PizzaStore:
    def __init__(self, factory):
        self.factory = factory

    def order_pizza(self, pizza_type):
        # Use the factory to create a pizza
        pizza = self.factory.create_pizza(pizza_type)

        # Prepare the pizza
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


if __name__ == "__main__":
    # Create a pizza factory
    factory = SimplePizzaFactory()

    # Create a pizza store with the factory
    store = PizzaStore(factory)

    # Order a Cheese Pizza
    print("Ordering a Cheese Pizza:")
    store.order_pizza("cheese")

    print("\nOrdering a Pepperoni Pizza:")
    # Order a Pepperoni Pizza
    store.order_pizza("pepperoni")
