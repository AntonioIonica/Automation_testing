"""
Sedan type with 2 sub-types:
    -Luxury sedan
    -Sport sedan
"""


class SedanCar:
    w_type = 'car'
    w_meaning = '4+1 doors and a separate trunk'

    def __init__(self, traction, gen, color, custom):
        self._traction = traction
        self._gen = gen
        self._color = color
        self._custom = custom

    def body_type(self):
        if self._traction == 'Rear traction':
            print('Your car is a sport oriented one!')
            if self._color == 'Custom':
                print('Option not available for Street package!')
            else:
                print('Option is available!')
        elif self._traction == '4x4 traction':
            print('Your engine will be upgraded to 400 HP!')
            if self._color == 'Custom':
                print('Option is available and it will cost 1500$ extra-charge!')
            else:
                print('Option is available!')
        else:
            print('You didn\'t chose a traction type!')

    def generation(self):
        if self._gen == 'Last gen' and self._custom == 'Custom body-kit':
            print('Your option is available and you have to chose your custom kit!')
        elif self._gen == '2021' and self._custom == 'Custom body-kit':
            print('You have to wait extra months for the car to be made!')
        else:
            print('Older generation are not available at this moment!')

        self.body_type()
        print(f'Your {SedanCar.w_type} is a {SedanCar.w_meaning} with extra options!')


class LuxurySedan(SedanCar):

    def auto_park(self):
        if self._gen == 'Last gen':
            print('You have the free option to upgrade to Auto-Parking!')
            pass

    def vip_package(self):
        if self._traction == '4x4 traction':
            print('Your car has been upgraded to free pair of wheels!')
        else:
            print('Your car has Michellin wheels')
        self.auto_park()


class SportSedan(SedanCar):

    def self_driving(self):
        if self._gen == 'Last gen':
            print('Your car will be upgraded to Self Autonomus driving!')
            pass

    def sport_plus(self):
        if self._traction == '4x4 traction':
            print('Your car will have a front engine!')
        else:
            print('Your car will have a rear positioned engine!')


sedan_car = SedanCar('4x4 traction', 'Last gen', 'Custom', 'Custom body-kit')
sedan_car.generation()
lux_car = LuxurySedan('4x4 traction', '2021', 'Black', 'Custom body-kit')
lux_car.vip_package()
sport_car = SportSedan('Rear traction', '2021', 'Custom', 'Custom body-kit')
sport_car.generation()
sport_car.sport_plus()
