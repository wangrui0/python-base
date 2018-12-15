# 列表中的extend和append 的使用
a = [1, 2, 3, 4, 5, 6]
b = [7, 8]
# extend 相当于合并
a.extend(b)
print(a)
# append相当于把一个整体进行添加
c = [1, 2, 3, 4, 5, 6]
d = [7, 8]
c.append(d)
print(c)
'''
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, [7, 8]]
'''

