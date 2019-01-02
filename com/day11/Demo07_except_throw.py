class Test(object):
    def __init__(self, switch):
        self.switch = switch  # 开关

    def cal(self, a, b):
        try:
            return a / b
        except Exception as result:
            if self.switch:
                print("捕获到异常啦，如下：")
                print(result)
            else:  # 重新抛出异常，此时就不会被这个异常处理器给捕获。从而处罚默认的异常处理
                raise


# test1 = Test(True)
# test1.cal(1, 0)
"""
捕获到异常啦，如下：
division by zero
================================
"""
print("=================注释上面的，执行下面的===============")
test1 = Test(False)
test1.cal(1, 0)
"""
=================注释上面的，执行下面的===============
Traceback (most recent call last):
  File "C:/File/2-workspace/python/python-base/com/day11/Demo07_except_throw.py", line 25, in <module>
    test1.cal(1, 0)
  File "C:/File/2-workspace/python/python-base/com/day11/Demo07_except_throw.py", line 7, in cal
    return a / b
ZeroDivisionError: division by zeros
"""

