class Dog(object):
    def __init__(self):
        print("init")

    def __del__(self):
        print("del")

    def __str__(self):
        print("str")

    #     def __new__(cls):
    #         print("new")
    #
    #
    # # 测试
    # dog = Dog()
    # """
    # new
    # """
    def __new__(cls):  # cls 此时是Dog指向的那个类的对象
        # print(id(cls))
        print("new")
        return object.__new__(cls)


# 测试
dog = Dog()
"""
new
init
del

"""
"""
注意：创建一个对象，相当于做了3件事：
1：调用__new__方法来创建对象，然后找一个变量来接受__new__的返回值，这个返回值表示的创建出来的对象的引用
2:__init__(刚刚创建出对象的引用)
3：返回对象的引用
new 方法决定了创建对象，init方法决定了，初始化对象
"""
