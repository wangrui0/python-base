"""
简单工厂的举例:
适用于单产品簇

"""


class CarStore(object):

    def __init__(self):
        self.factory = Factory()

    def order(self, car_type):
        return self.factory.select_car_by_type(car_type)


class Factory(object):
    def select_car_by_type(self, car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif car_type == "名图":
            return Mingtu()
        elif car_type == "ix35":
            return Ix35()


class Car(object):
    def move(self):
        print("车在移动....")

    def music(self):
        print("正在播放音乐....")

    def stop(self):
        print("车在停止....")


class Car(object):
    def move(self):
        print("车在移动....")

    def music(self):
        print("正在播放音乐....")

    def stop(self):
        print("车在停止....")


class Suonata(Car):
    def move(self):
        print("Suonata车在移动....")

    def music(self):
        print("Suonata正在播放音乐....")

    def stop(self):
        print("Suonata车在停止....")


class Mingtu(Car):
    def move(self):
        print("Mingtu车在移动....")

    def music(self):
        print("Mingtu正在播放音乐....")

    def stop(self):
        print("Mingtu车在停止....")


class Ix35(Car):
    def move(self):
        print("Ix35车在移动....")

    def music(self):
        print("Ix35正在播放音乐....")

    def stop(self):
        print("Ix35车在停止....")


car_store = CarStore()
car = car_store.order("索纳塔")
car.move()
car.music()
car.stop()
