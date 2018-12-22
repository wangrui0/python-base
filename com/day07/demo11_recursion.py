# 递归： 只举个简单的例子吧，计算：指定数字的阶乘
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(2))  # 2*1
print(factorial(3))  # 3*2*1
print(factorial(4))  # 4* 3* 2*1
print(factorial(5))  # 5*4*3*2*1
print(factorial(10))
'''
2
6
24
120
3628800

Process finished with exit code 0
'''
