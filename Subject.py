from abc import ABC, abstractmethod


# Subject (Observable) Interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass


# Concrete Subject (Weather Data)
class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


# Concrete Observer (Current Conditions Display)
class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)
        self.temperature = 0.0
        self.humidity = 0.0

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}°C and {self.humidity}% humidity")


if __name__ == "__main__":
    # Create the WeatherData (subject)
    weather_data = WeatherData()

    # Create observers
    current_display = CurrentConditionsDisplay(weather_data)

    # Simulate new weather measurements
    weather_data.set_measurements(25, 65, 1013)
    weather_data.set_measurements(28, 70, 1012)

