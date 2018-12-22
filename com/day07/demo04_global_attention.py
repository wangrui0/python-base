# 注意 全局变量定义的顺序：全局变量在函数调用之前定义就可以啦;故为了好看：我们一般在开头调用
a = 100


# b = 200
# c = 300


def test():
    print("a=%d" % a)
    print("b=%d" % b)
    print("c=%d" % c)


b = 200

test()

c = 300  # 有问题
'''
a=100
Traceback (most recent call last):
b=200
  File "C:/File/2-workspace/python/python-base/com/day07/demo04_global_attention.py", line 15, in <module>
    test()
  File "C:/File/2-workspace/python/python-base/com/day07/demo04_global_attention.py", line 10, in test
    print("c=%d" % c)
NameError: name 'c' is not defined
'''
