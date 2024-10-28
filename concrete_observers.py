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
