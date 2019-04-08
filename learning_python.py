'''
age = int(input('enter your age:'))
if age >= 18:
    print('your age is:',age)        #我是注释，哈哈哈哈哈哈
    print('adult')
else:
    print('滚吧，小屁孩！')

def fyf():
   """@fyf 我是文档，哈哈哈哈哈哈"""
#定义计算bmi的函数
def bmi(weight,height):
    bmi_temple = weight/height**2
    print('你的bmi指数是：%.4f' % bmi_temple)

    if bmi_temple < 18.5:
        print('过轻')
    elif 18.5 <= bmi_temple < 25:
        print('正常')
    elif 25 <= bmi_temple < 28:
        print('过重')
    elif 28 <= bmi_temple < 32:
        print('肥胖')
    else:
        print('严重肥胖')

weight = float(input('请输入你的体重(KG)：'))
height = float(input('请输入你的身高(M)：'))
bmi(weight,height)
'''

#closesure闭包函数
def outer(a):
#    a += 1
    def inner(b):
        nonlocal a
        a += 1
        return a+b
    return inner
demo1 = outer(1)
print(demo1(10))
print(demo1(10))
print(demo1(10))
print(demo1(10))
print(demo1(10))


classmates = ['李狗蛋','王二柱','范冰冰']
for name in classmates:
    print(name)


#计算1到9的和
count = 0
list1 = [1,2,3,4,5,6,7,8,9]
for x in list1:
    count = count + x
print(count)

#计算0到100的和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#求奇数和
sum = 0
n = 99
while n > 0:
    sum = sum + n #递归recursion
    n = n - 2
print(sum)

#求偶数和
sum = 0
n = 100
while n > 0:
    sum = sum + n #递归recursion
    n = n - 2
print(sum)

L = ['许三多','伊布拉西诺维奇','C罗']
for x in L:
    print('你好,',x)

#break用法
n = 0
while n < 100:
    if n > 9:
        break
    else:
        n = n + 1
        print(n)
print('END',n)

#死循环
'''
n = 0
while n == 0:
    print('go on')
'''


#dictionary字典 python内置dict字典
d = {'翠花':'100分','酸菜':'88分','狗蛋':'95分'}
print(d['翠花'])

d['翠花'] = '89分'
print(d['翠花'])

#dictionary.get( ),没有key,返回none,可自己设定返回值
print(d.get('王二麻子','俺们班没这人！'))
print(d.get('酸菜'))

print('王二麻子' in d)    #用in判断key是否存在,交互界面返回boolean值


#自定义一个绝对值函数
#x = float(input('求绝对值,请输入数字：'))
#x = 'a'
x = 11
def my_absolute(x):
    if not isinstance(x,(int,float)):
        raise TypeError('你输入的不是数字啊,傻逼！')
    if x >= 0:
        return x
    else:
        return -x
print(my_absolute(x))



#空函数
def empty():
   pass            #没想好写什么先写pass,不然运行会出错


import math

def move(x,y,r,sangle):
    nx = x + r*math.cos(sangle)
    ny = y + r*math.sin(sangle)
    return nx,ny

print(move(0,0,5,math.pi/6))        #返回一个tuple元组
x,y = move(0,0,5,math.pi/6)         #返回的其实还是一个tuple,并不是两个数
print(x,y)

q,z = 6,7
print(q,z)

print(math.sqrt(2))         #sqrt()求平方根函数,square root平方根



def nth_power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def employee(name,age,city='QinZhon',province='广西'):    #city是默认参数,默认参数只能放在必选参数后面
    print('name is:',name)                               #默认参数必须指向不变的对象
    print('age:',age)
    print('city:',city)
    print('province:',province)


employee('王铁柱',25)
employee('郭德纲',30,'火星')      #employee(city='长沙','李雷',22)  错误的调用
employee('光头强',40,province='黑龙江',city='沈阳')
#前两个位置参数须按顺序提供,后两个默认参数可以不按顺序提供,但要把参数名写上

#L = [ ]  列表本身是个可变对象，如果做默认参数的话有个问题，改变后默认参数也改变了

def add_list_end(l=None):
    if l is not None:
        l.append('END')
    else:
        l = []
    return l

l = []
print(add_list_end(l))


#计算a^2+b^2+c^2......+n^2的值
def nth_power(*x):               #可变参数 *x 参数前加*
    sum = 0
    for n in x:
        sum = sum + n * n
    return sum

print(type(nth_power(1,2,3,4,5)))       #可变参数在函数调用时自动封装成一个tuple
print(nth_power(5,7))



#关键字参数 **x  参数前加**
def person(name,age,**other):
    print('名字:',name,'年龄:',age,'其他：',other)

#key-value用关键字传入函数的**other参数,other将获得一个dict的拷贝
dict1 = {'A':11,'B':12}
person('王二狗',22,other1=dict1['A'],other2=dict1['B'])

#关键字参数在函数调用时自动封装成一个dict
person('面筋哥',40,性别='男',city='石家庄',weight=65)


person('面筋哥',40)

# x,y 位置(必选?)参数
# x=0 默认参数
# *x 可变参数
# **x关键字参数
# *,x1,x2 命名关键字参数   特殊分隔符*后为命名关键字参数
# *c,x1,x2   *c为可变参数,后面的命名关键字参数不再需要特殊分隔符*
#参数命名的顺序：可选参数,默认参数,可变参数,命名关键字参数,关键字参数

def product(x,y,*z):
    if z is None:
        sum = x * y
    else:
        sum_z = 1
        for i in z:
            sum_z = sum_z * i
        sum = x * y * sum_z
    return sum

# 可变参数后的命名关键数参数不再需要特殊分隔符*
# 命名关键字参数必须传入参数名e1=1,e2=2  与位置参数不同,不然会报错,要简化函数调用可设默认值e1=0,e2=0
def p1(a,b,c=0,*d,e1=0,e2=0,**f):
    print('a=',a,'b=',b,'c=',c,'d=',d,'e1=',e1,'e2=',e2,'f=',f)

def p2(a,b,c=0,*d,e1,e2):     # 特殊分隔符后面的e1,e2为命名关键字参数
    print('a=',a,'b=',b,'c=',c,'d=',d,'e1=',e1,'e2=',e2)


p1(1,2,5,6,7,'A',e2=5,e1=6,A=1,C=2)
p2(1,2,5,6,7,'A',e1=1,e2=2)
#p1(1,2,3,4,5,e1=6,e2=7)

#关键字参数返回dict
def p3(**b):
    print(b)
    return b

print(type(p3(b=2)))

#函数返回命名关键字参数的传入值的类型
def p4(*,a):
    print(a)
    return a

print(type(p4(a='A')))
print(type(p4(a=1)))

#..............................
def p5(*,a,b):
    print(a,b)
    print(b)
    return a,b

print(p5(a=1,b=1))
print(type(p5(a=1,b=1)))


#一个函数在函数内部调用函数自身，称为递归函数  recursion function
#阶乘factorial, n!=1*2...*(n-1)*n可推导出n!=n*(n-1)!   (0!=1 定义,无法推导出来)
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(0))
print(fact(1))
print(fact(5))

#注意：递归函数返回包含表达式,会有栈上溢的问题,递归太多次会溢出


#解决调用递归函数栈溢出的方法是进行尾递归优化,尾递归与循环效果一样，循环可看做特殊的尾递归函数
#尾递归是指,在函数返回时,函数调用函数自身,并且,return语句不能包含表达式(上例中的返回return语句就包含的表达式
#因此,有栈溢出的问题),这样,interpreter解释器就把尾递归做优化,使递归本身无论调用多少次,都是只占一个栈帧.

#def fact1(n):
#    return fact2(n,1)
def fact2(n,product=1):
    if n == 0:
        return product
    return fact2(n-1,n*product)

print(fact2(0))
print(fact2(1))
print(fact2(3))

#注意:python标准解释器并没有尾递归的优化,所以上面的函数并没有什么卵用,还是会栈溢出......


#利用slice切片进行字符串删减的函数,第一个动脑筋编写的函数,哈哈哈哈哈哈
def trim(a):
    n = len(a)
    s1 = ''
    for i in range(n):
        if a[i] == ' ':
            s1 = a[i+1:]  #list[a:b]切片包头不包尾,取索引a至b之间的元素,包含a,不包含b!
        else:             #这句可以去掉,但本人阅读起来逻辑不够直观
            break         #同上一句
    j = -1
    while s1[j] == ' ':
        s2 = s1[:j]      #切片不包尾,所以s1[:j]为取s1[j]之前的元素,不包含s1[j]
        j = j - 1
    return s2


print('去除首尾空格前:',' 23 56  ')
print('去除首尾空格后:',trim(' 23 56  '))
print('去除首尾空格前字符串长度:',len(' 23 56  '))
print('去除首尾空格后字符串长度:',len(trim(' 23 56  ')))


#dict字典也是可迭代iterable对象,dict的存储不是按list的方式顺序排列,
# 迭代出的结果顺序很可能不一样
d = {'a':1,'b':2,'c':3,'d':4,'a1':5,'b1':6}
for i in d:
    print(i)
#字符串也是可迭代对象
s = 'abc'
for i in s:
    print(i)

#python内建函数isinstance()用于检测对象的类型
#collections模块的iterable类型(可迭代对象)
#int float list tuple dict str这些都是python内建的类型

from collections import Iterable
print(isinstance('abcd',Iterable)) #is an instance of是给一个...的实例

#enumerate()为python内建函数,用它可以同时得到索引index和值value
for index,value in enumerate('abcdefg'):
    print(index,value)

#动脑子写的第二个函数,哈哈哈哈哈哈哈哈哈
def FindMixAndMac(L):
    if L == []:
        return (None,None)
    else:
        Mix = L[0]
        Max = L[0]
        for i in L:     #遍历列表L,迭代iteration
            if Mix > i: #Mix赋值为L[0],如果列表有比Mix小的,将该值赋予Mix
                Mix = i
        for j in L:
            if Max < j: #Max赋值为L[0],如果列表有比Max大的,将该值赋予Max
                Max = j
        return (Mix,Max)

L1 = [2,7,12,1,45]
L2 = []
L3 = [7]
L4 = [7,1]
print(FindMixAndMac(L1))
print(FindMixAndMac(L2))
print(FindMixAndMac(L3))
print(FindMixAndMac(L4))


#list comprehensions列表推导,多写几遍就记得语法了,可以简化循环
print([x * y for x in range(1,11) for y in range (5,21)])
print([x * y for x in range(1,3) for y in range (1,4)])
print([x * y for x in range(1,3) for y in range (1,4) if x * y % 2 == 0])


import os  #导入os模块:该模块就是对操作系统进行调用 operating system
print([l for l in os.listdir()])


dict2 = {'a':1,'b':2,'c':3}
for x in dict2:
    print(x)
for x in dict2.items():   #items()返回键值对元组数组
    print(x)


#作业,哈哈哈哈哈哈哈哈哈,又写完一个作业
L1 = ['hello','world',18,'apple',None]
L2 = [x for x in L1 if isinstance(x,str)]
print(L2)

#generator 生成器(单词翻译:发电机,电力公司,生产者)
#创建generator 生成器与list comprehensions 列表推导式的区别在于最外层的()和[]
#generator返回一个generator对象,list comprehensions返回一个列表,两个都是可迭代对象iterable
#generator返回的是算法,列表很大的话,占用的储存空间小,list comprehensions返回一个完整的列表,
g = (x for x in range(1,11))
print(next(g))                #通过next()打印generator生成器创建的对象
print(next(g))
print(next(g))

for n in g:                   #通过for循环遍历generator生成器创建的对象
    print(n)                  #打印元素

'''
def recursion(n):
        while n == None:
            n = n + 1
            print(n)
        return recursion(n)
recursion(1)
'''

#斐波那契数列
def fibonacci(x):
    n,a,b = 1,0,1
    while n <= x:
        print(b)
        a,b = b,a + b
        n = n + 1
    return 'done'
fibonacci(6)


def fibonacci1(x):
    n,a,b = 1,0,1
    while n <= x:
        yield b        #定义generator生成器的第二种方法,函数包含yield就是一个generator
        a,b = b,a + b   #yield 翻译:退位,退让
        n = n + 1
    return 'done'
print(fibonacci1(6))

for x in fibonacci1(6):
    print(x)


f = fibonacci1(2)
print(next(f))
print(next(f))
#print(next(f))

print('.......................')

g = (x for x in range(1,11))
def i_g(n):
    for x in g:
        if n > 0:
            print(x)
            n = n - 1
    return 'end'

i_g(3)

#可作用于for循环的是可迭代iterable对象
#可作用于for循环,还可以被next()调用返回一个值,直到StopIteration错误提示的,称为iterator迭代器

from collections import Iterable
#从collections模块导入Iterable类型 可迭代类型

print(isinstance((),Iterable)) #判断tuple元组是否is a instance of(一个...的实例)可迭代对象iterable
print(isinstance([],Iterable)) #list列表
print(isinstance({'A':1,'B':2},Iterable)) #dict字典(dictionary)
print(isinstance({'A','B'},Iterable)) #set
print(isinstance('',Iterable)) #str字符串(string)
print(isinstance([lc for lc in range(1,11)],Iterable)) #list comprehensions列表推导式
print(isinstance((g for g in range(1,11)),Iterable)) #generator生成器,与列表推导式的区别是[]和()

print('..........华丽的分割线..........')
from collections import Iterator
#从collections模块导入Iterator类型 迭代器类型

print(isinstance((),Iterator)) #同上,只是变成判断Iterator迭代器对象类型
print(isinstance([],Iterator))
print(isinstance({'A':1,'B':2},Iterator))
print(isinstance({'A','B'},Iterator))
print(isinstance('',Iterator))
print(isinstance([lc for lc in range(10)],Iterator))
#哈哈哈哈哈哈,上面六个都不能被next()函数调用
print(isinstance((g for g in range(1,11)),Iterator)) #只有generator能被next()函数调用

print('..........华丽的分割线..........')
#把tuple元组,list列表,dict字典,set,str字符串,list comprehensions等iterable对象
#变成iterator迭代器,可以使用iter()函数

print(isinstance(iter(()),Iterator)) #同上,只是变成判断Iterator迭代器对象类型
print(isinstance(iter([]),Iterator))
print(isinstance(iter({'A':1,'B':2}),Iterator))
print(isinstance(iter({'A','B'}),Iterator))
print(isinstance(iter(''),Iterator))
print(isinstance(iter([lc for lc in range(10)]),Iterator))


#iterator对象是一个数据流

#higher-order function(高阶函数)
#变量可以指向函数,例如：f = abs,函数的参数能接受变量function(x,y)
#那么一个函数可以接收另一个函数作为参数,这种函数称之为高阶函数.
#abs(-120)是函数调用,abs是函数本身
print('......高阶函数higher-order funciton......')
def add(x,y,f):
    return f(x) + f(y)
x = 15
y = -10
f = abs

print(add(x,y,f))

#map(mapped映射),reduce归约(减少,缩小,使还原)
#map(),reduce()是python内置的高阶函数

def f(x):
    return x * x
#map()函数接收两个参数,一个是函数,一个是Iterable
#map()函数将传入的函数依次作用到序列的每个元素,结果返回Iterator
print(map(f,range(1,11)))
r = map(f,range(1,11))
print(next(r))
print(next(r))
print(next(r))
print(next(r))









