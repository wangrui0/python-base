"""
异常的传递--try嵌套中
"""
import time

try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print('关闭⽂件')
except:
    print("没有这个⽂件")
"""
没有这个⽂件
"""
"""
函数嵌套调⽤中
"""


def test1():
    print("----test1-1----")
    print(2 / 0)
    print("----test1-2----")


def test2():
    print("----test2-1----")
    test1()
    print("----test2-2----")


def test3():
    try:
        print("----test3-1----")
        test1()
        print("----test3-2----")
    except Exception as result:
        print("捕获到了异常，信息是:%s" % result)
        print("----test3-2----")


test3()
print("------华丽的分割线-----")
test2()
"""
捕获到了异常，信息是:division by zero
----test3-2----
------华丽的分割线-----
  File "C:/File/2-workspace/python/python-base/com/day11/Demo09_except_transfer.py", line 32, in test2
----test2-1----
----test1-1----
    test1()
  File "C:/File/2-workspace/python/python-base/com/day11/Demo09_except_transfer.py", line 28, in test1
    print(2/0)
ZeroDivisionError: division by zero
"""
"""
总结：
如果try嵌套，那么如果⾥⾯的try没有捕获到这个异常，那么外⾯的try会
接收到这个异常，然后进⾏处理，如果外边的try依然没有捕获到，那么
再进⾏传递。。。
如果⼀个异常是在⼀个函数中产⽣的，例如函数A---->函数B---->函数C,
⽽异常是在函数C中产⽣的，那么如果函数C中没有对这个异常进⾏处
理，那么这个异常会传递到函数B中，如果函数B有异常处理那么就会按
照函数B的处理⽅式进⾏执⾏；如果函数B也没有异常处理，那么这个异
常会继续传递，以此类推。。。如果所有的函数都没有处理，那么此时
就会进⾏异常的默认处理，即通常⻅到的那样
注意观察上图中，当调⽤test3函数时，在test1函数内部产⽣了异常，此
异常被传递到test3函数中完成了异常处理，⽽当异常处理完后，并没有
返回到函数test1中进⾏执⾏，⽽是在函数test3中继续执⾏
"""
