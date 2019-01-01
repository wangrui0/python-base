from com.day11.factoryMethod.factory.BMWCarFactory import BMWCarFactory
from com.day11.factoryMethod.store.Store import Store


class BMWCarStore(Store):
    def select_car(self, car_type):
        return BMWCarFactory().select_car_by_type(car_type)
