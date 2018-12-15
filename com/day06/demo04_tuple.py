# 元组和列表很类似，不同之处在于元组的元素是不可以修改的，元组使用小括号，列表使用中括号。字典使用大括号
# 列表增删改查都可以
nums = [1, 2, 3, 4, 5]
print(type(nums))  # <class 'list'>
# 元组不能改哦，只可以是查
nums2 = (1, 2, 3, 4, 5)
print(type(nums2))  # <class 'list'>
# nums2[0] = 1
'''
<class 'list'>
Traceback (most recent call last):
<class 'tuple'>
  File "C:/File/workspace/python/python-base/com/day06/demo04_tuple.py", line 8, in <module>
    nums2[0] = 1
TypeError: 'tuple' object does not support item assignment
'''
