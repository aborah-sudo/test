# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass
