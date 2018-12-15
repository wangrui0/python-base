# 字典列表的使用--名片管理系统管理系统
print("=" * 60)
print("名片管理系统 V0.01")
print("1 添加名片")
print("2 删除名片")
print("3 修改名片")
print("4 查询名片")
print("5 遍历名片")
print("6 退出系统")
print("=" * 60)
card_cases = []  # 存储
while True:
    num = int(input("请输入序号:"))
    if num == 1:  # 添加名片
        card_case = {}  # 创建一个空的字典，用于存储数据
        new_name = input("请输入名字")
        new_qq = input("请输入qq号")
        new_age = input("请输入年龄")
        card_case["name"] = new_name
        card_case["qq"] = new_qq
        card_case["age"] = new_age
        card_cases.append(card_case)
        print("添加成功，结果为")
        print(card_cases)
    elif num == 2:  # 删除名片
        name = input("请输入要删除的名片的名字")
        flag = False  # 默认不在列表中
        for card_case in card_cases:
            if card_case["name"] == name:
                card_cases.remove(card_case)
                flag = True
                print("删除成功")
                print(card_cases)
        if not flag:
            print("%s不在列表中" % name)
        pass
    elif num == 3:  # 修改名片
        name = input("请输入要修改的名片的名字")
        new_qq = input("请输入要修改的名片的age")
        new_age = input("请输入要修改的名片的qq")
        for card_case in card_cases:
            if card_case["name"] == name:
                card_case['qq'] = new_qq
                card_case['age'] = new_age
                flag = True
        if not flag:
            print("%s不在列表中" % name)
    elif num == 4:  # 查询名片
        name = input("请输入要查询的名片的名字")
        flag = False  # 默认不在列表中
        for card_case in card_cases:
            if card_case["name"] == name:
                print("name     age     qq      ")
                print("%s       %s      %s" % (card_case["name"], card_case["age"], card_case["qq"]))
                flag = True
        if not flag:
            print("%s不在列表中" % name)
    elif num == 5:  # 遍历名片
        for card_case in card_cases:
            print("name     age     qq      ")
            print("%s       %s      %s" % (card_case["name"], card_case["age"], card_case["qq"]))
    elif num == 6:  # 退出系统
        break
    else:
        print("输入错误，请重新输入")
