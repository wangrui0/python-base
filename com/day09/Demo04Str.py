class Cat:
    """
    init 初始化方法的定义
    """

    # 属性
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    # 方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):
        print("%s的年龄是:%d" % (self.name, self.age))

    # str 的使用，相当于java 中的toString方法
    def __str__(self):
        return "%s的年龄是:%d" % (self.name, self.age)


# 创建一个对象
tom = Cat("tom", 18)

# 调用tom指向的对象中的 方法
tom.eat()
tom.drink()
print(tom)
"""
猫在吃鱼....
猫正在喝kele.....
tom的年龄是:18
"""
