# 判断键盘输入的性别
sex = input("请输入性别：男，女,或者中性")
if sex == "男":
    print("你是一个男性")
elif sex == "女":
    print("你是一个女性")
# elif sex == "中性":
else:
    print("你是中性")
# 判断键盘输入的是星期几
num = int(input("请输入（1-7）"))
if num == 1:
    print("星期一")
elif num == 2:
    print("星期二")
elif num == 3:
    print("星期三")
elif num == 4:
    print("星期四")
elif num == 5:
    print("星期五")
elif num == 6:
    print("星期六")
elif num == 7:
    print("星期天")
else:
    print("输入错误")
