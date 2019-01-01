from com.day11.factoryMethod.entity.Mingtu import Mingtu
from com.day11.factoryMethod.entity.Ix35 import Ix35
from com.day11.factoryMethod.entity.Suonata import Suonata


class XianDaiFactory(object):
    def select_car_by_type(self, car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif car_type == "名图":
            return Mingtu()
        elif car_type == "ix35":
            return Ix35()