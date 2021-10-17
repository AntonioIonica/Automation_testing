"""
Vehicle
"""

from OOP_vehicle_model import VehicleBlueprint


class Vehicle(VehicleBlueprint):
    """
    _get_option
    """

    # atribute de clasa, nu depind de obiect
    w_type = 'car'
    w_brand = 'Volkswagen'

    def __init__(self, model, year, color, motor, ):  # initializarea clasei
        self._model = model  # encapsularea = ascunderea informatiei. Se face cu _cuvant
        self._year = year  # nu ai acces la anumite metode prin encapsulare
        self._color = color
        self._motor = motor

    def self_driving_car(self):
        self.driving()

    def get_wheels(self):
        pass

    def waypoints(self):
        return self.driving() + ' break on c'

    def _get_option(self, motor_value):  # TODO de folosit doar _get_option in loc de toate if de jos
        if motor_value == '1.2':  # TODO alte if-uri aici sau direct range-uri
            print('Option avilable!')
        elif motor_value == '1.4':
            print('Option avilable!')
        else:
            print('You need to upgrade to Sport or Luxury package!')

    def _set_motor(self):
        if self._model == 'Golf':
            self._get_option(self._motor)

        elif self._model == 'Touareg':
            if self._motor == '1.6':
                print('Option avilable!')
            elif self._motor == '2.0':
                print('Option avilable!')
            else:
                print('You need to upgrade to Sport package!')

        else:
            if self._motor == '2.2':
                print('Option avilable!')
            elif self._motor == '2.4':
                print('Option avilable!')
            else:
                print('You don\'t care about the planet')

    def config(self, package):
        if package == 'Default':
            print('You chose the Default package!')

        elif package == 'Sport':
            print('You chose the Sport package!')

        else:
            print('You chose the Luxury package!')

        self._set_motor()

        print(f'Your {Vehicle.w_brand} {Vehicle.w_type} is a {self._model} model,'
              f' year {self._year}, with {self._color} and {self._motor} engine!')


my_car = Vehicle('Golf', '2020', 'Black', '2.0')
my_car.config('Sport')
print(my_car.__doc__)
my_car.driving()
x = my_car.waypoints()
print(x)

# TODO minim 2 child class SUV and berline si fiecare cu alte 2 class copii
