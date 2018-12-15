# 字符串之切片
name = "abcdefABCDEF"

print("=======正序=======")
# 举例
print(name[0])  # a
print(name[0:2])  # ab
# 取头不取尾
print(name[0:3])  # abc
print(name[0:4])  # abcd
# 品味一下
print(name[0:-2])  # abcdefABCD
print(name[0:-1])  # abcdefABCDE
# 从第二个取到最后
print(name[1:])  # bcdefABCDEF
# 按步长取
print(name[1:8:1])  # [开始下标：结束下标：步长] bcdefAB 等价于print(name[1:8]) 如果不写步长，步长的默认值都是1
print(name[1:8:2])  # [开始下标：结束下标：步长]  bdfB --->相当于循环中的，步长.(其实是一个意思)
# 逆序
print("=======逆序=======")
print(name[0:])  # 正序 abcdefABCDEF
print(name[0::1])  # 正序 abcdefABCDEF 根据步长取找的
print(name[::1])  # 正序 abcdefABCDEF 根据步长取找的
print(name[-1:])  # F
print(name[-1:0])  # ''
print(name[-1:0:-1])  # FEDCBAfedcb
print(name[-1::-1])  # FEDCBAfedcba
print(name[::-1])  # FEDCBAfedcba
'''
感悟：
切片或者是逆序其实是根据步频来决定的，也就是第三个参数。
如果是正数：
第一个位置，是开始位置从左面开始
第二个位置，是结束位置是右边
第三个位置是步频
举例：
name[1:8:2] ：2为正数，意味着，从左到右，第一个位置开始，到第8个位置，步频为2
如果是负数:
第一个位置，是开始位置，从右面开始
第二个位置，是结束位置是左面
第三个位置是步频
举例：
name[-1:0:-1]:2为负数，意味着，从右到左，从右面第一个位置到左面第0个位置，步频为1
如果不写：默认正数
'''
