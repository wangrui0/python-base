#  while 和 for  变量列表
nums = [1, 2, 3, 4, 5, 6]
# while 遍历
i = 0
print("while遍历")
while i < len(nums):
    print(nums[i])
    i += 1
print("for遍历")
for num in nums:
    print(num)
