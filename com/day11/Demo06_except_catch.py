# try:  # try 和catch中存放怀疑会出现异常的代码(如果当发生异常时，程序没有捕获该异常，程序将会终止，当捕获住异常时，程序会调到异常代码，然后执行异常捕获后的代码)
#     num = 2 / 0
#     print(num)
#     print("aaa")
# except NameError:  # 捕获的异常的类型
#     print("已经捕获到异常")  # 异常捕获后，的处理；
# print("程序执行结束")
"""
Traceback (most recent call last):
  File "C:/File/2-workspace/python/python-base/com/day11/Demo06_except.py", line 2, in <module>
    num = 2 / 0
ZeroDivisionError: division by zero

"""
try:  # try 和catch中存放怀疑会出现异常的代码(如果当发生异常时，程序没有捕获该异常，程序将会终止，当捕获住异常时，程序会调到异常代码，然后执行异常捕获后的代码)
    num = 2 / 0
    print(num)
    print("aaa")
except ZeroDivisionError:  # 捕获的异常的类型
    print("已经捕获到异常")  # 异常捕获后，的处理；
print("程序执行结束")
"""
已经捕获到异常
程序执行结束
"""
