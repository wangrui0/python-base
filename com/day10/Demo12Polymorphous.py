class Dog(object):
    """
    多态：
    （1）存在继承关系
    （2）父类的引用指向子类的对象（python是弱类型的语言，这点比较的弱）
    （3）调用重写的方法

    """

    def print_self(self):
        print("大家好,我是xxxx,希望以后大家多多关照....")


class Xiaotq(Dog):
    def print_self(self):
        print("hello everybody, 我是你们的老大,我是xxxx")


def introduce(temp):
    temp.print_self()


dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)
"""
大家好,我是xxxx,希望以后大家多多关照....
hello everybody, 我是你们的老大,我是xxxx
"""
