class Dog(object):
    __instane = None

    def __new__(cls, *args, **kwargs):
        if cls.__instane == None:
            cls.__instane = object.__new__(cls)
            return cls.__instane
        else:
            return cls.__instane

    def __init__(self, name):
        self.name = name


dog1 = Dog("旺财")  # 创建了dog对象，并调用__init__方法，初始化 旺财
print(dog1.name)
dog2 = Dog("哮天犬")  # 使用dog对象，并调用__init__方法，重新初始化哮天犬
print(dog2.name)
print(dog1.name)  # 已经被重新初始化为哮天犬
"""
创建对象一次，但是初始化了两次，也就是__init__方法执行力两次
dog
旺财
哮天犬
哮天犬
"""
