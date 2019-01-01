from com.day11.factoryMethod.entity.Mini import Mini

from com.day11.factoryMethod.entity.SuvX6 import SuvX6


class BMWCarFactory(object):
    def select_car_by_type(self, car_type):
        if car_type == "mini":
            return Mini()
        elif car_type == "x6":
            return SuvX6()
