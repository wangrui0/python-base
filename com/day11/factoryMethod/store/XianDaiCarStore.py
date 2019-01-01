from com.day11.factoryMethod.factory.XianDaiFactory import XianDaiFactory
from com.day11.factoryMethod.store.Store import Store


class XianDaiCarStore(Store):
    def select_car(self, car_type):
        return XianDaiFactory().select_car_by_type(car_type)
