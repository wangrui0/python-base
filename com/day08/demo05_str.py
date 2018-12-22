# 字符串常⻅操作
# 如有字符串	mystr	=	'hello	world	itcast	and	itcastcpp'	，以下是常⻅ 的操作
mystr = 'hello	world	itcast	and	itcastcpp'
# <1>find
# 检测	str	是否包含在	mystr中，如果是返回开始的索引值，否则返回-1
print(mystr.find("itcast"))  # 12
mystr.find("itcast", 0, 20)  # 12
# <2>index
# 跟find()⽅法⼀样，只不过如果str不在	mystr中会报⼀个异常.
mystr.index("itcast")  # 12
# mystr.index("itcas2222t")
'''
Traceback (most recent call last):
  File "C:/File/2-workspace/python/python-base/com/day08/demo05_str.py", line 11, in <module>
    mystr.index("itcas2222t")# 12
ValueError: substring not found
'''
# <3>count
# 返回	str在start和end之间	在	mystr⾥⾯出现的次数
print(mystr.count("itcast", 0, len(mystr)))  # 2
# <4>replace
# 把	mystr	中的	str1	替换成	str2,如果	count	指定，则替换不超过	count	次.
print(mystr.replace("itcast", "itddd", mystr.count("itcast")))  # hello	world	itddd	and	itdddcpp
# <5>split
# 以	str	为分隔符切⽚	mystr，如果	maxsplit有指定值，则仅分隔	maxsplit	个⼦ 字符串
print(mystr.split("	", 2))  # ['hello', 'world', 'itcast\tand\titcastcpp']
print(mystr.split("	"))  # ['hello', 'world', 'itcast', 'and', 'itcastcpp']
# <6>capitalize
# 把字符串的第⼀个字符⼤写
print(mystr.capitalize())  # Hello	world	itcast	and	itcastcpp
# <7>title
# 把字符串的每个单词⾸字⺟⼤写
print(mystr.title())  # Hello	World	Itcast	And	Itcastcpp
# <8>startswith
# 检查字符串是否是以	obj	开头,	是则返回	True，否则返回	False
print(mystr.startswith("hello"))  # True
print(mystr.startswith("dllo"))  # False
# <9>endswith
# 检查字符串是否以obj结束，如果是返回True,否则返回	False.
print(mystr.endswith("itcastcpp"))  # True
# <10>lower
# 转换	mystr	中所有⼤写字符为⼩写
print(mystr.lower())  # hello	world	itcast	and	itcastcpp
# <11>upper
# 转换	mystr	中的⼩写字⺟为⼤写
print(mystr.upper())  # HELLO	WORLD	ITCAST	AND	ITCASTCPP
# <12>ljust
# 返回⼀个原字符串左对⻬,并使⽤空格填充⾄⻓度	width	的新字符串
print(mystr.ljust(300))
# <13>rjust
# 返回⼀个原字符串右对⻬,并使⽤空格填充⾄⻓度	width	的新字符串
print(mystr.rjust(20))
# <14>center
# 返回⼀个原字符串居中,并使⽤空格填充⾄⻓度	width	的新字符串
print(mystr.center(3000))
# <15>lstrip
# 删除	mystr	左边的空⽩字符
# mystr.lstrip()
# <16>rstrip
# 删除	mystr	字符串末尾的空⽩字符
# mystr.rstrip()
# <17>strip
# 删除mystr字符串两端的空⽩字符
# python基础语⾔
# 114字 符串常⻅操作
# >>>	a	=	"\n\t	itcast	\t\n" >>>	a.strip() 'itcast'
# <18>rfind
# 类似于	find()函数，不过是从右边开始查找.
# mystr.rfind(str,	start=0,end=len(mystr)	)
# <19>rindex
# 类似于	index()，不过是从右边开始.
# mystr.rindex(	str,	start=0,end=len(mystr))
# <20>partition
# 把mystr以str分割成三部分,str前，str和str后
# mystr.partition(str)
# <21>rpartition
# 类似于	partition()函数,不过是从右边开始.
# mystr.rpartition(str)
# <22>splitlines
# 按照⾏分隔，返回⼀个包含各⾏作为元素的列表
# mystr.splitlines()
# <23>isalpha
# 如果	mystr	所有字符都是字⺟	则返回	True,否则返回	False
# mystr.isalpha()
# <<24>isdigit
# 如果	mystr	只包含数字则返回	True	否则返回	False.
# mystr.isdigit()
# <25>isalnum
# 如果	mystr	所有字符都是字⺟或数字则返回	True,否则返回	False
# mystr.isalnum()
# <26>isspace
# 如果	mystr	中只包含空格，则返回	True，否则返回	False.
# mystr.isspace()
# <27>join
# mystr	中每个字符后⾯插⼊str,构造出⼀个新的字符串
# mystr.join(str)
#
