from abc import ABC,abstractmethod

class vehicle(ABC):
    def __init__(self,n):
        self.n=n
    @abstractmethod
    def start(self):
        pass
