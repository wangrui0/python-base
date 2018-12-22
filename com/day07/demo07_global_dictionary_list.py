# 字典和列表作为全局变量
nums = [11, 22, 33]
infor = {"name": "laowang"}


def test():
    # for num in nums:
    #    print(num)

    nums.append(44)
    infor['age'] = 18


def test2():
    print(nums)
    print(infor)


test()
test2()
'''
[11, 22, 33, 44]
{'name': 'laowang', 'age': 18}
'''

