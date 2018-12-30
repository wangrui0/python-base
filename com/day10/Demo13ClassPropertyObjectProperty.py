"""
实现记录创建对象个数的功能

"""


class Tool(object):
    def __init__(self, new_name):
        self.name = new_name


# 底下这个方法太笨啦
num = 0
tool1 = Tool("铁锹")
num += 1
print(num)
tool2 = Tool("工兵铲")
num += 1
print(num)
tool3 = Tool("水桶")
num += 1
print(num)

"""
1
2
3
"""


class Tool2(object):
    """
    实例属性为某个类所有，对象共有

    """
    # 类属性
    num = 0

    # 方法
    def __init__(self, new_name):
        # 实例属性
        self.name = new_name
        # 对类属性+=1
        Tool2.num += 1


# 这个比较好
tool1 = Tool2("铁锹")
tool2 = Tool2("工兵铲")
tool3 = Tool2("水桶")

print(Tool2.num)
"""
3
"""
