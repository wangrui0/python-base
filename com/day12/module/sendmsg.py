"""
__all__的使用
注入：模块使用中有个缺陷：
比如：from sendmsg import *
那么sendmsg中的所有的东西都会被暴露，怎么才能只暴露指定的东西呢？
__all__的使用 这个全局变量写的是谁，那么其他导入这个包的，那个文件只能用谁
"""

__all__ = ["test1", "num", "Test"]


def test1():
    print("-----test1----")


def test2():
    print("-----test2----")


num = 0
num2 = 0


class Test(object):
    pass


class Test2(object):
    pass


# __开头 __结尾，一般都是系统的方法
if __name__ == "__main__":  # 这__name__非常的独特，不同的文件调用他，值不一样。当前文件调用他为__main__其他文件调用他为导入的文件名称
    test1()
    test2()
