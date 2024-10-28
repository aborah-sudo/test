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
