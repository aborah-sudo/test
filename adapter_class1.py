from abc import ABC, abstractmethod


# Concrete Duck
class MallardDuck():
    def quack(self):
        print("Quack!")

    def fly(self):
        print("I'm flying long distances!")


# Concrete Turkey
class WildTurkey():
    def gobble(self):
        print("Gobble gobble!")

    def fly_short_distance(self):
        print("I'm flying a short distance!")


# Turkey Adapter
class TurkeyAdapter():
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        # Turkeys fly short distances, so we call it multiple times
        for _ in range(5):
            self.turkey.fly_short_distance()


if __name__ == "__main__":
    # Create a MallardDuck
    mallard_duck = MallardDuck()
    print("The Duck says:")
    mallard_duck.quack()
    mallard_duck.fly()

    # Create a WildTurkey
    wild_turkey = WildTurkey()
    print("\nThe Turkey says:")
    wild_turkey.gobble()
    wild_turkey.fly_short_distance()

    # Use a TurkeyAdapter to make the Turkey behave like a Duck
    turkey_adapter = TurkeyAdapter(wild_turkey)
    print("\nThe TurkeyAdapter (as a Duck) says:")
    turkey_adapter.quack()
    turkey_adapter.fly()
