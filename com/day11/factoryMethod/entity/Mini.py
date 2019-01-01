from com.day11.factoryMethod.entity.Car import Car


class Mini(Car):
    def move(self):
        print("Mini车在移动....")

    def music(self):
        print("Mini正在播放音乐....")

    def stop(self):
        print("Mini车在停止....")
