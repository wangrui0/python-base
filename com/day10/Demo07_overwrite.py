class Animal:
    def eat(self):
        print("-----吃----")

    def drink(self):
        print("-----喝----")

    def sleep(self):
        print("-----睡觉----")

    def run(self):
        print("-----跑----")


class Dog(Animal):
    def bark(self):
        print("----汪汪叫---")


class Xiaotq(Dog):
    def fly(self):
        print("----飞----")

    def bark(self):
        print("----狂叫-----")


xiaotq = Xiaotq()
print(Xiaotq.mro())  # 或者xiaota.__mro__或打印继承的顺序
xiaotq.fly()
xiaotq.bark()
xiaotq.eat()
"""
[<class '__main__.Xiaotq'>, <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>]
----飞----
----狂叫-----
-----吃----
"""
