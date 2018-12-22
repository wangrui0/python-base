# 不定长的参数
def sum_2_nums(a, b, *args):
    print("-" * 30)
    print(a)
    print(b)
    print(args)

    result = a + b
    for num in args:
        result += num
    print("result=%d" % result)


sum_2_nums(11, 22, 33, 44, 55, 66, 77)
sum_2_nums(11, 22, 33)
sum_2_nums(11, 22)
# sum_2_nums(11)#错误,因为 形参中 至少要2个实参
'''
------------------------------
11
22
(33, 44, 55, 66, 77)
result=308
------------------------------
11
22
(33,)  这点需要注意呀，一个元素的元组应该加个逗号
result=66
------------------------------
11
22
()
result=33

Process finished with exit code 0
'''
