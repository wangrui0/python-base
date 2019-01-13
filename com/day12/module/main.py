"""
__all__的使用
注入：模块使用中有个缺陷：
比如：from sendmsg import *
那么sendmsg中的所有的东西都会被暴露，怎么才能只暴露指定的东西呢？
__all__的使用
"""
from com.day12.module.sendmsg import *

# test1()
# test = Test()
# print(num)
"""
-----test1----
0
"""
test2()
"""
Traceback (most recent call last):
  File "C:/File/2-workspace/python/python-base/com/day12/module/main.py", line 17, in <module>
    test2()
NameError: name 'test2' is not defined
"""
