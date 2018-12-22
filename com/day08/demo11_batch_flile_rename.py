# 文件夹下的重命名
# 1 请输入文件夹
import os

'''
folder_name = input("请输入文件夹名称")
# 2 获取那个文件夹下的所有的文件名
file_names = os.listdir(folder_name)
os.chdir(folder_name)  # 切换到这个文件夹下
# 对文件名进行重命名就可以
for file_name in file_names:
    print(file_name)
    os.rename(file_name, "[测试]-" + file_name)
'''
folder_name = input("请输入文件夹名称")
# 2 获取那个文件夹下的所有的文件名
file_names = os.listdir(folder_name)
# 对文件名进行重命名就可以
for file_name in file_names:
    print(file_name)
    new_file_name = "./" + folder_name + "/" + file_name
    old_file_name = "./" + folder_name + "/" + "[测试]-" + file_name
    os.rename(new_file_name, old_file_name)
