# 文件的copy(大文件的读取)
# 1获取要复制的文件名
old_file_name = input("请输入文件名（注意需要输入文件的后缀）")
# 2 打开要复制的文件
old_file = open(old_file_name, "r")
# 3 创建一个新的文件
# 3.1 创建新的文件名称 假如：原来的文件名称为：老文件.txt -->老文件[复制].txt
position = old_file_name.rfind(".")
new_file_name = old_file_name[0:position] + "[复制2]" + old_file_name[position:]
new_file = open(new_file_name, "w")
# 4 从old 文件中，读取数据，写入到new 文件中
# content = old_file.read()
# new_file.write(content)
while True:
    content = old_file.read(1024)
    if len(content) != 0:
        new_file.write(content)
    else:
        break
# 5关闭两个文件
old_file.close()
new_file.close()
