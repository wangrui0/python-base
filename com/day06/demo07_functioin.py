# 定义一个无参数的构造函数
def print_triangle():
    print("*" * 1)
    print("*" * 2)
    print("*" * 3)
    print("*" * 4)
    print("*" * 5)


# 定义一个有参数的构造函数
def sum(a, b):
    print("%d+%d=%d" % (a, b, (a + b)))


# 调用无参数的构造函数
print_triangle()
# 调用有参数的构造函数
num1 = int(input("请输入num1:"))
num2 = int(input("请输入num2:"))
sum(num1, num2)
