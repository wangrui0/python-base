# 交换两个变量 a,b
a = 2
b = 3
c = -1
print("交换前a: %d,b:%d" % (a, b))
# 方式一：
# c = a
# a = b
# b = c
# print("交换后a: %d,b:%d" % (a, b))  #交换后a: 3,b:2
'''
交换前a: 2,b:3
交换前a: 3,b:2
'''
'''
交换方式二：
'''
# a = a + b
# b = a - b
# a = a - b
# print("交换后a: %d,b:%d" % (a, b))#交换后a: 3,b:2
'''
交换方式三：
'''
a, b = b, a
print("交换后a: %d,b:%d" % (a, b))  # 交换后a: 3,b:2
