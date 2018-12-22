# 目前所学的当中，只有列表和字典是可变的，其余的都不是
# 数字 不可变类型
a = 100


def test(num):
    num += num
    print(num)


test(a)

print(a)
'''
200
100
说明了什么呢？将a 指向的值给num，然后num执行  num += num，num值重新指向了200，a指向的100仍然没有变化
(100是个不可变类型，那我新建一个哦)
'''

# 字符串
# 元组
c = (100,)  # 不可变类型


def test1(num):
    num += num
    print(num)


test1(c)

print(c)
'''
(100, 100)
(100,)
'''
# 列表 可变类型
b = [100]


def test2(num):
    num += num
    print(num)


test2(b)

print(b)
'''
[100, 100]
[100, 100]
'''
# 注意啊:
d = [100]


def test3(num):
    # 1. 先算 =号右边的
    # 2. 算出来的结果是[100,100]
    # 3. num = [100,100]    num+=num num=num+num  这俩不是真正的等级的哦
    # 4. 让num变量指向了[100,100],即num保存的是[100,100]的引用(内存地址)
    num = num + num  # num=num+num ========>[100]  + [100]====>[100,100]  注意python中的任意一个等号，都是指向哦
    print(num)


test3(d)

print(d)
'''
[100, 100]
[100]

注意哦
 num+=num num=num+num  这俩不是真正的等级的哦
 （1）num=num+num ========>[100]  + [100]====>[100,100]  先计算等号右面的(新开辟一个内存空间)，然后让等号左边的指向右边的，注意python中的任意一个等号，都是指向哦
 （2）num+=num 这个是直接修改num的值哦
'''
# 字典
