class Dog:
    def set_age(self, new_age):
        if new_age > 0 and new_age <= 100:
            self.age = new_age
        else:
            self.age = 0

    def get_age(self):
        return self.age


dog = Dog()
# 不隐藏属性(假设人的年龄为0岁到100岁，-10 正确么？)
dog.age = -10
print(dog.age)
# 隐藏对象的属性(方法中对属性进行检查)
dog.set_age(-10)
age = dog.get_age()
print(age)
"""
-10
0
"""
