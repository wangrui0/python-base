# 局部变量
def test01():
    a = 10
    print("a=%d" % a)


def test02():
    print("a=%d" % a)


# 全局变量
test01()
test02()
'''
a=10
Traceback (most recent call last):
  File "C:/File/workspace/python/python-base/com/day07/demo01_variable.py", line 13, in <module>
    test02()
  File "C:/File/workspace/python/python-base/com/day07/demo01_variable.py", line 8, in test02
    print("a=%d" % a)
NameError: name 'a' is not defined
'''
