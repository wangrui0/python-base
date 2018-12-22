# coding=utf-8
# 匿名函数的应用一：

def test(a, b, func):
    result = func(a, b)
    print(result)


test(11, 22, lambda x, y: x + y)

'''
执行流程
test(11, 22, lambda x, y: x + y)-->def test(a, b, func):
func=lambda x, y: x + y
result =func(a, b)
'''
# 匿名函数的应用二：从键盘输入一个匿名函数
'''
    这个程序完成了从键盘输入一个匿名函数,这个匿名函数就会被执行
    这体现了python语言的动态性,即在运行的时候才确定功能,而不是写完之后功能就确定了
'''


def test2(a, b, func):
    result = func(a, b)
    print(result)


# python2中不需要使用eval,因为python2中,input输入的内容就当做一个表达式
# python3 需要使用eval对字符串转换一下,转为 一个表达式
func_new = input("请输入一个匿名函数:")
func_new = eval(func_new)

test2(11, 22, func_new)
'''
请输入一个匿名函数:lambda x,y : x+y
33

Process finished with exit code 0
'''
