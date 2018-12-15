"""
举例：打印
*
**
***
****
*****
"""
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
# 注意print 打印完后就立马换行
print("*", end="")
# 或者
print("*", end='')
print()
"""
打印9*9乘法表
"""
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d*%d=%d     " % (col, row, col * row), end="")
        col += 1
    print()
    row += 1
