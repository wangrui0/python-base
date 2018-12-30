class Base(object):
    """
    多继承在java中是不可用的，但是在python中是可以的。他的继承顺序有自己的一套遍历规范（这对数据结构有一定的要求哦）
    要尽量避免父类有相同的方法名的情况（否则得考研你的数据结构啦）

    """

    def test(self):
        print("----Base")


class A(Base):
    def test(self):
        print("-----A")


class B(Base):
    def test(self):
        print("-----B")


class C(A, B):
    pass
    # def test(self):
    #    print("-----C")


c = C()
c.test()

print(C.__mro__)
"""
-----A
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
"""
