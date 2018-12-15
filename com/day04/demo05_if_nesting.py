# if 嵌套  注意：else 和对应tab键匹配的相对应（空格）
# 举例一：
ticket = 1  # 1:是已经买票，0:是没有买票
knifeLength = 8  # cm 刀子的长度
if ticket == 1:
    print("你已经购买票了,请进安检")
    if knifeLength <= 10:
        print("安检过了，请进站！")
    else:
        print("安检没过过,有违禁物品！")
else:
    print("你每买票啊")
'''
你已经购买票了,请进安检
安检过了，请进站！
'''
# 举例二： 打印高富帅和白富美


