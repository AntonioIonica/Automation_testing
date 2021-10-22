"""
SUV type with 2 sub-types:
    -Super luxury suv
    -Electric SUV
"""


class SuvCar:
    w_type = 'car'
    w_meaning = 'Sport Utility Vehicle'
    w_traction = '4x4 drive'

    def __init__(self, car_body, gen, color, custom):
        self._car_body = car_body
        self._gen = gen
        self._color = color
        self._custom = custom

    def body_type(self):
        if self._car_body == 'Family body':
            print('Your car will have 7 seats and 3500$ extra-charge!')
            if self._color == 'Custom':
                print('Option not available for Family pack!')
            else:
                print('Option is available!')
        elif self._car_body == 'Sport package':
            print('Your engine will be upgraded to 600 HP!')
            if self._color == 'Custom':
                print('Option is available and it will cost 1500$ extra-charge!')
            else:
                print('Option is available!')
        else:
            print('You didn\'t chose a car body!')

    def generation(self):
        if self._gen == '2021' and self._custom == 'Custom body-kit':
            print('Your option is available and you have to chose your custom kit!')
        elif self._gen == '2020' and self._custom == 'Custom body-kit':
            print('You have to wait extra months for the car to be made!')
        else:
            print('Older generation are not available at this moment!')

        self.body_type()
        print(f'Your {SuvCar.w_type} is a {SuvCar.w_meaning} with {SuvCar.w_traction}!')


class SuperLuxury(SuvCar):

    def auto_park(self):
        if self._gen == '2021':
            print('You have the free option to upgrade to Auto-Parking!')
            pass

    def vip_package(self):
        if self._car_body == 'Sport':
            print('The VIP-Package will grant an extra-isolation for the back seats!')
        else:
            print('Your car has massage seats!')


class ElecSUV(SuvCar):

    def self_driving(self):
        if self._gen == '2021':
            print('Your car will be upgraded to Self Autonomus driving!')
            pass

    def tri_motors(self):
        if self._car_body == 'Sport package':
            print('Your car will have 3 electric engines!')
        else:
            print('Your car will have 2 electric engines!')


suv_car = SuvCar('Sport package', '2021', 'Custom', 'Custom body-kit')
suv_car.generation()
super_lux = SuperLuxury('Sport package', '2020', 'Custom', 'Custom body-kit')
super_lux.auto_park()
elec_suv = ElecSUV('Sport package', '2021', 'Custom', 'Custom body-kit')
elec_suv.generation()
elec_suv.tri_motors()
