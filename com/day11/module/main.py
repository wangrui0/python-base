# from com.day11.module import sendmsg, recvmsg
# 从某个包，导入对应的模块
# sendmsg.test1()
# sendmsg.test2()
# recvmsg.test1()


from com.day11.module.sendmsg import test1, test2
from com.day11.module.sendmsg import test2

# 从包里面的某个模块导入方法（注意：后导入的将会把新导入的替换；比如test2）
# from sendmsg import *
# from recvmsg import *

test1()
test2()
