# 拆包是针对元组
tuple = (1, 2)
# 输出方式一：
print(tuple[0])
print(tuple[1])
# 输出方式二：拆包
a, b = tuple
print(a)
print(b)
'''
1
2
1
2
'''
