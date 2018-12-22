# 文件的写
file = open("test.txt", "w")
file.write("haha")
file.close()

# 文件的读
file = open("test.txt", "r")
str = file.read()
print(str)
file.close()
# 简单的应用
