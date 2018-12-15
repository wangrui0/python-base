# （1） 字典的定义
# info ={键:值，键：值}
info = {"name": "张三", "age": 18, "addr": "山东"}
print(info)
print("name:%s,age:%d,addr:%s" % (info["name"], info["age"], info["addr"]))
'''
{'name': '张三', 'age': 18, 'addr': '山东'}
name:张三,age:18,addr:山东
字典和列表的区别：
相同点：
  都可以用于存储数据
不同点：
  列表通过下标取元素，字典通过key取元素
'''
# (2) 字典的增删改查
infors = {"name": "李四"}
# 增加(只要这个key不存在，就是添加)
infors["age"] = 18
print(infors)  # {'name': '李四', 'age': 18}
# 改(只要这个key存在，就是修改)
infors['name'] = "王五"
print(infors)  # {'name': '王五', 'age': 18}
# 删除（只需要写key就行，只是如果没有key，那么程序将会报错）
del infors["name"]
print(infors)  # {'age': 18}
# 查询（只需要写key就行，只是如果没有key，那么程序将会报错）
print(infors["age"])  # 18
# 查询2（只需要写key就行，如果没有key报错）
print(infors.get("age"))  # 18
