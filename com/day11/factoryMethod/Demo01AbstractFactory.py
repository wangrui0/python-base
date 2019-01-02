
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

"""
Mini车在移动....
Mini正在播放音乐....
Mini车在停止....
SUVX6车在移动....
SUVX6正在播放音乐....
SUVX6车在停止....
Mingtu车在移动....
Mingtu正在播放音乐....
Mingtu车在停止....

"""
