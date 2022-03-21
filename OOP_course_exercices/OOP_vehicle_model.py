"""
Abstractizare
Crearea modelului de vehicul
"""
from abc import ABC, abstractmethod


# abstractbaseclass

class VehicleBlueprint(ABC):
    @abstractmethod  # modifica comportamentul metode
    def _get_option(self, motor_value):
        raise NotImplemented

    @abstractmethod
    def self_driving_car(self):
        raise NotImplemented

    @abstractmethod
    def get_wheels(self):
        raise NotImplemented

    def driving(self):
        return 'We need to go from A to B!'
