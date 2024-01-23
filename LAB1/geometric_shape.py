from abc import ABC, abstractmethod

class GeometricShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
