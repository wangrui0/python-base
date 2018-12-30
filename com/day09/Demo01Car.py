class Cat:  # class 标志一个类
    def eat(self):  # def 方法的标志
        print("Cat eat")

    def drink(self):
        print("Cat drink")

    def introduec(self):
        print("i amo a cat,my name is %s,i am %d years old" % (self.name, self.age))
        self.eat()
        self.drink()


cat = Cat()
# 使用方法
cat.eat()
cat.drink()
# 添加属性
cat.name = "小花"
cat.age = 18
print(cat.name)
print(cat.age)
print("===========")
cat.introduec()#相当于 cat.introduce(cat)
'''
输出：
Cat eat
Cat drink
小花
18
===========
i amo a cat,my name is 小花,i am 18 years old
Cat eat
Cat drink

Process finished with exit code 0

'''
