"""

集合：里面的内容不允许重复哦

"""
"""
元组
(1, 2, 3)
<class 'tuple'>
"""
a = (1, 2, 3)
print(a)
print(type(a))
"""
列表
[1, 2, 3]
<class 'list'>
"""
b = [1, 2, 3]
print(b)
print(type(b))

"""
集合
{1, 2, 3}
<class 'set'>
"""
c = {1, 2, 3}
print(c)
print(type(c))
"""
举例将列表去重
"""
"""法一"""
d = [1, 1, 2, 2, 3, 4]
c = []
for num in d:
    if num not in c:
        c.append(num)
print(c)  # [1, 2, 3, 4]
"""法二采用集合去重复"""
e = list(set(d))
print(e)  # [1, 2, 3, 4] set(d) 将列表转为集合,list()将集合转为列表
