from abc import ABC, abstractmethod

class Car(ABC):

    def home(self):
        print("this is piyush home")

    @abstractmethod
    def speed(self):
        pass


class Honda(Car):

    def speed(self):
        print("speed is 100")


class maruti(Car):

    def speed(self):
        print("speed is 100")

obj = Honda()
obj.home()
obj.speed()

