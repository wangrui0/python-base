def test1():
    print("-----test1----")

def test2():
    print("-----test2----")
#__开头 __结尾，一般都是系统的方法
if __name__ == "__main__":#这__name__非常的独特，不同的文件调用他，值不一样。当前文件调用他为__main__其他文件调用他为导入的文件名称
    test1()
    test2()
