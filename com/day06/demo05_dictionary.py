# 字典的使用
info = {"name": "张三", "age": 18}
# 求键值对的长度
print(len(info))  # 2 键值对的长度
# 求所有的键的集合（Pythons2（键的列表） 和python3（对象） 返回的是不一样的类型）
key_list = info.keys()
print(type(key_list))  # <class 'dict_keys'> 对象
print(key_list)  # dict_keys(['name', 'age'])
# 求值的集合
value_list = info.values()
print(type(value_list))  # <class 'dict_values'>对象
print(value_list)  # dict_values(['张三', 18])
# 求键值对的集合
item_list = info.items()
print(type(item_list))  # <class 'dict_items'>对象
print(item_list)  # dict_items([('name', '张三'), ('age', 18)]) 列表中每个元素是一个元组
# 遍历字典方式一：通过键值对的集合遍历字典
for key in key_list:
    print(key + "-->" + str(info[key]))
'''
name-->张三
age-->18
'''
# 遍历字典方式二：
for item in item_list:
    print(item[0] + "-->" + str(item[1]))
'''
name-->张三
age-->18
'''
# 使用拆包进行遍历
for a, b in item_list:
    print(a + "-->" + str(b))
