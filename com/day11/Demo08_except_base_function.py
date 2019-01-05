try:
    num = input("XXX:")
    int(num)
    print("=============")
except NameError:
    print("出现了名字异常，出现异常的处理为。。。。。。。。。")
except(FileNotFoundError, ZeroDivisionError):
    print("出现了文件未找到或者被除数为0的异常，出现异常的处理为...........")
except Exception as ret:
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常,这个except一定会捕获到")
else:
    print("没有异常才会执行的功能")
finally:
    print("------finally-----")
print("-----2----")
"""
XXX:2
=============
没有异常才会执行的功能
------finally-----
-----2----
"""
"""
XXX:we
如果用了Exception,那么意味着只要上面的except没有捕获到异常,这个except一定会捕获到
------finally-----
-----2----
"""
