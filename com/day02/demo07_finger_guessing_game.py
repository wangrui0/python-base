"""
实现猜拳游戏，知道猜中才退出
"""
import random

while True:
    num = int(input("请输入：剪刀(0),石头(1),布（2）"))
    computer = random.randint(0, 2)
    if (num == 0 and computer == 2) or (num == 1 and computer == 0) or (num == 2 and computer == 1):
        print("恭喜呀，你输入的是:%d,电脑输入的是：%d，你赢了" % (num, computer))
        break
    elif num == computer:
        print("你和电脑输入的都是:%d" % num)
    else:
        print("你输啦，你输入的是:%d,电脑输入的是：%d" % (num, computer))
