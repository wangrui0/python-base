# if or 的使用
you = input("你去吗？")  # 去或者不去
wife = input("你老婆去吗？")  # 去或者不去
if you == "去" or wife == "去":
    print("你和你老婆有一个去啦，A事情办成了")
# if and 的使用
if you == "去" and wife == "去":
    print("你和你老婆都去了，B事情办成了")
#  白富美测试
color = input("你白么？")  # 白或者黄
money = int(input("你富有？"))  # 1000
beautiful = input("你美么？")  # 美
if color == "白" and money >= 100000000 and beautiful == "美":
    print("白富美")
    print("好羡慕")
else:
    print("矮穷矬")
    print("矮穷矬")
'''
not 的使用

'''

if not (color == "白" and money >= 100000000 and beautiful == "美"):
    print("矮穷矬")
    print("矮穷矬")
else:
    print("白富美")
    print("好羡慕")
