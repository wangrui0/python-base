# 每次读取f一行数据
file = open("demo01_anonymous_function.py", "r", encoding='UTF-8')
data_line = file.readline()
while len(data_line) != 0:
    data_line = file.readline()
    # print(data_line, end='')
'''
def test(a, b):
    a + b


result1 = test(11, 22)
print("result1=%s" % result1)

# 匿名函数只能完成很简单的功能,如果需要完成复杂的功能,请使用def定义的函数
# 定义一个匿名函数
func = lambda a, b: a + b
# 匿名函数默认会把 冒号后面的表达式的结果返回

result2 = func(11, 22)
print("result2=%s" % result2)


result1=None
result2=33

Process finished with exit code 0
'''
# 读取多行数据到一个列表中，每个元素是一行
file2 = open("demo01_anonymous_function.py", "r", encoding='UTF-8')
data_lines = file2.readlines()
for data_line in data_lines:
    print(data_line, end='')
'''
# 较为复杂的功能,需要使用def定义的函数
def test(a, b):
    a + b


result1 = test(11, 22)
print("result1=%s" % result1)

# 匿名函数只能完成很简单的功能,如果需要完成复杂的功能,请使用def定义的函数
# 定义一个匿名函数
func = lambda a, b: a + b
# 匿名函数默认会把 冒号后面的表达式的结果返回

result2 = func(11, 22)
print("result2=%s" % result2)

result1=None
result2=33

Process finished with exit code 0

'''
