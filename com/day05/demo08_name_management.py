# 列表的使用--名字管理系统
print("=" * 60)
print("名片管理系统 V0.01")
print("1 添加名字")
print("2 删除名字")
print("3 修改名字")
print("4 查询名字")
print("5 退出系统")
print("=" * 60)
names = []  # 存储数组
while True:
    num = int(input("请输入序号:"))
    if num == 1:
        name = input("请输入名字")
        names.append(name)
        print(names)
    elif num == 2:
        name = input("请输入要删除的名字")
        if name in names:
            names.remove(name)
            print("删除元素成功，列表结果为")
            print(names)
        else:
            print("列表中没有%s姓名" % name)
    elif num == 3:
        name = input("请输入要修改的名字")
        index = names.index(name)
        if index > -1:
            destName = input("请输入要修改为")
            names[index] = destName
            print("修改元素成功，列表结果为")
            print(names)
        else:
            print("列表中没有%s姓名" % name)
    elif num == 4:
        name = input("请输入要查询的名字")
        if name in names:
            print("%s在名字列表中" % name)
        else:
            print("%s不在名字列表中" % name)
    elif num == 5:
        break
    else:
        print("输入错误，请重新输入")
