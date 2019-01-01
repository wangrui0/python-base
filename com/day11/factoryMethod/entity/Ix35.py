from com.day11.factoryMethod.entity.Car import Car


class Ix35(Car):
    def move(self):
        print("Ix35车在移动....")

    def music(self):
        print("Ix35正在播放音乐....")

    def stop(self):
        print("Ix35车在停止....")