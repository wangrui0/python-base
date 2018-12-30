class Animal:
    """
    定义一个父类，python中继承其实很简单，定义一个父类，在子类定义类时，类名后面加上（父类），那么父类的方法和属性都会被子类继承（除了特殊情况）

    """

    def eat(self):
        print("-----吃----")

    def drink(self):
        print("-----喝----")

    def sleep(self):
        print("-----睡觉----")

    def run(self):
        print("-----跑----")


class Dog(Animal):
    """
    def eat(self):
        print("-----吃----")
    def drink(self):
        print("-----喝----")
    def sleep(self):
        print("-----睡觉----")
    def run(self):
        print("-----跑----")
    """

    def bark(self):
        print("----汪汪叫---")


class Cat(Animal):
    def catch(self):
        print("----抓老鼠----")


# a = Animal()
# a.eat()

wangcai = Dog()
wangcai.eat()

tom = Cat()
tom.eat()
"""
-----吃----
-----吃----

"""
