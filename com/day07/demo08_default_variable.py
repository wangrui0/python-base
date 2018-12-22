# 缺省参数 b 如果缺省时，默认传22，c如果缺省时，默认传33
def test(a, b, c=22, d=33):
    print("===================")
    print(a)
    print(b)
    print(c)
    print(d)


test(2, 3)
test(2, 3, 44)
test(2, 3, 44, 55)
test(2, 3, c=44, d=55)
test(c=2, a=3, b=44, d=55)  # 不按顺序，指定传值
'''
C:\File\2-workspace\python\python-base\venv\Scripts\python.exe C:/File/2-workspace/python/python-base/com/day07/demo08_default_variable.py
===================
2
3
22
33
===================
2
3
44
33
===================
2
3
44
55
===================
2
3
44
55
===================
3
44
2
55

Process finished with exit code 0

'''
