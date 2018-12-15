# for  else 的使用
nums = [1, 2, 3, 4, 5]
# 场景一：
for num in nums:
    if num == 2:
        print("这是2")
    else:
        print(num)
else:
    print("打印else")
'''
1
这是2
3
4
5
打印else
'''
# 场景二：
for num in nums:
    if num == 2:
        print("这是2")
        break
    else:
        print(num)
else:
    print("打印else")
'''
1
这是2
'''
'''
for-else-是一个组合：
如果for 中执行break 将不会执行else ,如果for 中不执行break将会执行else
'''
# 应用：
info = [{"name": "张三", "age": 18}, {"name": "李四", "age": 20}, {"name": "王五", "age": 24}]
name = input("请输入要查找的姓名")
for temp in info:
    if temp["name"] == name:
        print("找到%s了" % name)
        break
else:
    print("没有找到%s" % name)
'''
测试一：
请输入要查找的姓名张三
找到张三了
测试二：
请输入要查找的姓名david
没有找到david
'''
