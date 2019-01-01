
# 测试宝马
from com.day11.factoryMethod.store.BMWCarStore import BMWCarStore
from com.day11.factoryMethod.store.XianDaiCarStore import XianDaiCarStore

store1 = BMWCarStore()
mini = store1.order("mini")
mini.move()
mini.music()
mini.stop()
x6 = store1.order("x6")
x6.move()
x6.music()
x6.stop()
# 测试现代
store1 = XianDaiCarStore()
mingtu = store1.order("名图")
mingtu.move()
mingtu.music()
mingtu.stop()

#
# car_store = CarStore()
# car = car_store.order("索纳塔")
# car.move()
# car.music()
# car.stop()
