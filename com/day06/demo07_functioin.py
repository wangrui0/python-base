# 定义一个无参数的构造函数
def print_triangle():
    print("*" * 1)
    print("*" * 2)
    print("*" * 3)
    print("*" * 4)
    print("*" * 5)


# 定义一个有参数的构造函数
def sum_two(a, b):
    print("%d+%d=%d" % (a, b, (a + b)))


# return 的使用,定义一个函数，计算三个数值的加法
def sum_three(a, b, c):
    result = a + b + c
    return result


# return 返回多个值
def return_method(a, b, c):
    temp1 = [a, b, c]  # 列表
    temp2 = (a, b, c)  # 元组
    return temp1  # 返回列表


# return temp2  # 返回元组
# return (a, b, c)  # 返回元组
# return a, b, c  # 返回元组

# 函数的嵌套调用， 完成三个值的平均值的计算
def avg_three(a, b, c):
    result = sum_three(a, b, c)
    result /= 3
    print("%d,%d,%d 平均值为：%d" % (a, b, c, result))


# 调用无参数的构造函数
print_triangle()
# 调用有参数的构造函数
num1 = int(input("请输入num1:"))
num2 = int(input("请输入num2:"))
num3 = int(input("请输入num3:"))
sum_two(num1, num2)
sum_three(num1, num2, num3)
avg_three(num1, num2, num3)
