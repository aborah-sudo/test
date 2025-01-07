from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Light Receiver
class Light:
    def on(self):
        print("The light is ON.")

    def off(self):
        print("The light is OFF.")


# Fan Receiver
class Fan:
    def start(self):
        print("The fan is STARTED.")

    def stop(self):
        print("The fan is STOPPED.")


# Light On Command
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


# Light Off Command
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


# Fan Start Command
class FanStartCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.start()

    def undo(self):
        self.fan.stop()


# Fan Stop Command
class FanStopCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.stop()

    def undo(self):
        self.fan.start()


# Remote Control
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()


if __name__ == "__main__":
    # Create receivers
    living_room_light = Light()
    ceiling_fan = Fan()

    # Create commands
    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)
    fan_start = FanStartCommand(ceiling_fan)
    fan_stop = FanStopCommand(ceiling_fan)

    # Create remote control
    remote = RemoteControl()

    # Test the light commands
    print("Testing Light Commands:")
    remote.set_command(light_on)
    remote.press_button()
    remote.press_undo()

    remote.set_command(light_off)
    remote.press_button()
    remote.press_undo()

    # Test the fan commands
    print("\nTesting Fan Commands:")
    remote.set_command(fan_start)
    remote.press_button()
    remote.press_undo()

    remote.set_command(fan_stop)
    remote.press_button()
    remote.press_undo()
