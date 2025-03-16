from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


class NoQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You inserted a quarter.")
        self.gumball_machine.set_state(self.gumball_machine.has_quarter_state)

    def eject_quarter(self):
        print("You haven’t inserted a quarter.")

    def turn_crank(self):
        print("You turned, but there’s no quarter.")

    def dispense(self):
        print("You need to pay first.")


class HasQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can’t insert another quarter.")

    def eject_quarter(self):
        print("Quarter returned.")
        self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)

    def turn_crank(self):
        print("You turned the crank...")
        self.gumball_machine.set_state(self.gumball_machine.sold_state)
        self.gumball_machine.dispense()

    def dispense(self):
        print("No gumball dispensed.")


class SoldState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we’re already giving you a gumball.")

    def eject_quarter(self):
        print("Sorry, you already turned the crank.")

    def turn_crank(self):
        print("Turning twice doesn’t get you another gumball!")

    def dispense(self):
        self.gumball_machine.release_gumball()
        if self.gumball_machine.count > 0:
            self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)
        else:
            print("Oops, out of gumballs!")
            self.gumball_machine.set_state(self.gumball_machine.sold_out_state)


class SoldOutState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Machine is sold out. You can’t insert a quarter.")

    def eject_quarter(self):
        print("You can’t eject, you haven’t inserted a quarter yet.")

    def turn_crank(self):
        print("You turned, but there are no gumballs.")

    def dispense(self):
        print("No gumball dispensed.")


class GumballMachine:
    def __init__(self, count):
        self.count = count
        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)

        self.state = self.sold_out_state if count == 0 else self.no_quarter_state

    def set_state(self, state):
        self.state = state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()

    def dispense(self):
        self.state.dispense()

    def release_gumball(self):
        if self.count > 0:
            print("A gumball comes rolling out...")
            self.count -= 1


if __name__ == "__main__":
    machine = GumballMachine(3)

    # Insert a quarter and turn the crank
    print("\nScenario 1: Buying a gumball")
    machine.insert_quarter()
    machine.turn_crank()

    # Try turning crank without inserting a quarter
    print("\nScenario 2: Turning crank without a quarter")
    machine.turn_crank()

    # Insert a quarter and eject it
    print("\nScenario 3: Inserting and ejecting a quarter")
    machine.insert_quarter()
    machine.eject_quarter()

    # Buying all gumballs
    print("\nScenario 4: Buying remaining gumballs")
    machine.insert_quarter()
    machine.turn_crank()

    machine.insert_quarter()
    machine.turn_crank()

    # Machine should be sold out now
    print("\nScenario 5: Trying to use a sold-out machine")
    machine.insert_quarter()
    machine.turn_crank()
