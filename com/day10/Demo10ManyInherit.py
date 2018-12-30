class Base(object):
    """
    多继承在java中是不可用的，但是在python中是可以的。他的继承顺序有自己的一套遍历规范（这对数据结构有一定的要求哦）

    """

    def test(self):
        print("----Base")


class A(Base):
    def test1(self):
        print("-----test1")


class B(Base):
    def test2(self):
        print("-----test2")


class C(A, B):
    pass


c = C()
c.test1()
c.test2()
c.test()
"""
-----test1
-----test2
----Base
"""
