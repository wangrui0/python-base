from com.day11.factoryMethod.entity.Car import Car


class SuvX6(Car):
    def move(self):
        print("SUVX6车在移动....")

    def music(self):
        print("SUVX6正在播放音乐....")

    def stop(self):
        print("SUVX6车在停止....")