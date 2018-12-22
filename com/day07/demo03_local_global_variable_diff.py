'''

局部变量
def get_wendu():  # 如果一个函数有返回值,但是没有在调用函数之前 用个变量保存的话,那么没有任何的意义
    wendu = 33
    return wendu
def print_wendu(wendu):
    print("温度是：%d" % wendu)
result = get_wendu()
print_wendu(result)

'''

# 定义一个全局变量
temperature = 0


# def get_temperature():
#     temperature = 33  # 注意这只是新定义了一个局部变量
def get_temperature():
    global temperature
    temperature = 33


def print_temperature():
    print("温度是：%d" % temperature)


get_temperature()
print_temperature()
# 如果temperature这个变量已经在全局变量的位置定义了,此时还想在函数中对这个全局变量进行修改的话
# 那么 仅仅是 temperature=一个值  这还不够,,,此时temperature这个变量是一个局部变量,仅仅是和全局变量的名字
# 相同罢了

# 使用global用来对一个全局变量的声明,那么这个函数中的temperature=33就不是定义一个局部变量,而是
# 对全局变量进行修改
