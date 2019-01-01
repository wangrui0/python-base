from com.day11.factoryMethod.entity.Car import Car


class Suonata(Car):
    def move(self):
        print("Suonata车在移动....")

    def music(self):
        print("Suonata正在播放音乐....")

    def stop(self):
        print("Suonata车在停止....")