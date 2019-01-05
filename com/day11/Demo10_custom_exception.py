"""

你可以⽤raise语句来引发⼀个异常。异常/错误对象必须有⼀个名字，且它们
应是Error或Exception类的⼦类
"""


class ShortInputException(Exception):
    '''⾃定义的异常类'''

    def __init__(self, length, atleast):
        # super().__init__()
        self.length = length
        self.atleast = atleast
        """
        这⼀⾏代码，可以调⽤也可以不调⽤，建议调⽤，因
        为 __init__ ⽅法往往是⽤来对创建完的对象进⾏初始化⼯作，如
        果在⼦类中重写了⽗类的 __init__ ⽅法，即意味着⽗类中的很多
        初始化⼯作没有做，这样就不保证程序的稳定了，所以在以后的开
        发中，如果重写了⽗类的 __init__ ⽅法，最好是先调⽤⽗类的这
        个⽅法，然后再添加⾃⼰的功能
        """


def main():
    try:
        s = input('请输⼊ --> ')
        if len(s) < 3:
            # raise引发⼀个你定义的异常
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:  # x这个变量被绑定到了错误的实例
        print('ShortInputException: 输⼊的⻓度是 %d,⻓度⾄少应是 %d' % (result.length, result.atleast))
    else:
        print('没有异常发⽣.')


main()
"""
请输⼊ --> 2324
没有异常发⽣.
"""
"""
请输⼊ --> 2
ShortInputException: 输⼊的⻓度是 1,⻓度⾄少应是 3

"""
