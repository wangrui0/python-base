class Game(object):
    # 类属性
    num = 0

    # 实例方法(必须得有参数，)
    def __init__(self):
        # 实例属性
        self.name = "laowang"

    # 实例方法(必须得有参数(第一个参数传递的是当前的对象))
    # def __init__(a):
    #     # 实例属性
    #     a.name = "laowang"

    # 类方法（类拥有，对象共有。必须得有参数(第一个参数传递的是当前的对象)）
    @classmethod
    def add_num(cls):
        cls.num = 100

    # 静态方法（可以有参数，可以没参数）
    @staticmethod
    def print_menu():
        print("----------------------")
        print("    穿越火线V11.1")
        print(" 1. 开始游戏")
        print(" 2. 结束游戏")
        print("----------------------")


game = Game()
# Game.add_num()#可以通过类的名字调用类方法
game.add_num()  # 还可以通过这个类创建出来的对象 去调用这个类方法
print(Game.num)

# Game.print_menu()#通过类 去调用静态方法
game.print_menu()  # 通过实例对象 去调用静态方法
"""
100
----------------------
    穿越火线V11.1
 1. 开始游戏
 2. 结束游戏
----------------------
"""
