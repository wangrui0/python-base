class A:
    """
    私有属性在继承中的体现:
    注意：私有的属性和方法只在父类中可见，在子类中是不可见的。如果想使用父类中私有的属性或者方法，必须在父类中提供非私有
    的方法去访问父类中的私有的属性和方法

    """

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print("-----test1----")

    def __test2(self):
        print("-----test2----")

    def test3(self):
        self.__test2()
        print(self.__num2)


class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)


b = B()
# b.test1()
# b.__test2() #私有方法并不会被继承
# print(b.num1)
# print(b.__num2)拍
b.test3()
b.test4()
print(b.__num2)
"""
Traceback (most recent call last):
-----test2----
  File "C:/File/2-workspace/python/python-base/com/day10/Demo09PrivatePropertyInInherite.py", line 34, in <module>
200
    b.test4()
  File "C:/File/2-workspace/python/python-base/com/day10/Demo09PrivatePropertyInInherite.py", line 24, in test4
    self.__test2()
AttributeError: 'B' object has no attribute '_B__test2'
"""
