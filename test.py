#def input_digit_game():
#    i = input('input digit:')
#    while i != 'exit':
#        try:
#            a = float(i)
#        except:
#            a = '要输入数字啊！英文看不懂吗？'
#        print(a)
#        i =input('input digit again:')
#    print ('不玩滚！')
#    
#
#input_digit_game()

#def outter(msg='haha'):
#    def inner(x):
#        print(msg + x)
#    return inner
#
#f = outter()
#print(f)
#print(f.__name__)
#print(f('hehe'))

#class person(object):
#    name = 'fyf'
#    age = 99
#
#p1 = person
#print(p1.age)
#print(p1.__name__)

#dict = {
#    'id':123456789,
#    'name':'Li Lei',
#    'age': 16
#}
#
#def person(**dict):
#    return dict
#
#temp1 = person(dict=dict)
#print(temp1)
#print(temp1['dict'])
#print('>>>>>>>>>>>>>>>>>>>')
#temp2 = temp1['dict']
#print(temp2)
#print(temp2['id'])

#temp2 = person(**dict)
#print(temp2['id'])

#if True:
#    print(person(**dict))   #关键字参数，传入0或N个 含参数名的参数（例如：key1='xxx'，key2=18）,函数内部自动封装成一个字典
#    print(person(dict=dict))#运行可看到两者的区别
#else:
#    print('nothing')

#all() #built-in function内置函数，判定可迭代参数是否为True   除了 0，空，None ，false外都为True    注意：空tuple 空list也为True

#list1 = [1,2,False,4,5]
#print(all(list1))
#
#list2 = []
#tuple1 = ()
#
#print(all(list2))
#print(all(tuple1))

#>>>>>>>>>>>>>>>>>>>对call函数的理解>>>>>>>>>
# if x       x为非 0  (‘ ‘  空)   None  False
#x = 1
#
#def a():
#    if not x:           #not x作为条件,x表示    为 0   '  ' 空  None  False    
#        print('flase')
#    else:
#        print('true')
#
#a()
#>>>>>>>>>>>>>>>>>>>对call函数的理解>>>>>>>>>

#from wtforms import StringField
#
#u = StringField('fyf')
#print(dir(u))


#from class_example.subpackage import testmoudle
##from class_example.subpackage.testmoudle import test_class  #经实验，import不能跨两级目录
#
#t = testmoudle.test_package()
#t
#
#
#class A(testmoudle.test_class):
#    name2='class A'
#
#b = A()
#print(b.name)
#print(b.name2)
#
#print('OK')


#class Students():
#    #构建函数
#    def __init__(self,name,age,score):   #self实例变量，python解释器会自动传入实例名参数，类中的函数定义与普通函数的区别，加入self实例变量
#        self.name=name
#        self.age=age
#        self.__score=score    #变量名前加两个下划线，外部不能直接调用，相当与私有变量，python并没有真正意义上的私有变量,，具体看廖雪峰官方网站，太麻烦懒得写了，简单来说是python解释器解释是改变了该变量名
#
#    def get_name(self):
#        return self.name    #其实外部也可以self,name直接获取该属性，也可以外部直接修改self,name='xxx'
#
#    def get_score(self):
#        return self.__score  #“私有变量”，外部不能直接调用，可通过这个类class的方法method（本质是在类内定义的函数function）调用
#
#    def set_score(self,score):
#        if 0 <= score <= 100:
#            self.__score=score     #python解释器会把它解释成_Students__score变量，不同版本不一定相同，只需要知道有这么回事就行了，不要使用，所以外部self.__score=11相当于给对象增加了一个属性__score，类中定义的__score没影响
#        else:
#            raise ValueError('ValueError')

#std1=Students('fyf',18,98)
#print(std1.name)
#print(std1.get_score())
#
#std1.name='fff'
#print(std1.name)
#
##std1.set_score(88)
#std1.set_score('fyf')
#print(std1.get_score())


#定义class类就是定义一种数据类型，Animal和   list   string一样都是数据类型
#class Animal():  #基类，父类   base class    这叫做继承
#    def run(self):
#        print('Animal is running...')
#
#class Dog(Animal): #继承基类Animal 
#    pass
#
#class Cat(Animal):
#    pass
#
#
#dog1=Dog()
#cat1=Cat()
#
#print(dog1.run)
#print(cat1.run)
#    
#dog1.run()
#cat1.run()

#class Animal():  #基类，父类   base class
#    def run(self):
#        print('Animal is running...')
#
#class Dog(Animal): #继承基类Animal 
#    def run(self):  #subclass子类的run()会覆盖父类base class的run()方法   这叫做多态
#        print('Dog is running...')
#
#class Cat(Animal):
#    def run(self):
#        print('Cat is running...')
#
#dog1=Dog()
#cat1=Cat()
#
#dog1.run()
#cat1.run()


#def add_candle(f):
#    def insert_candle():
#        return f() + ' insert candle'
#    return insert_candle
#
#
#@add_candle
#def make_cake():
#    return 'cake'
#
#x = make_cake()
#print(x)


#slots  投放
#class Students():
#    __slots__=('name','age')     #限制类只能绑定name，age属性，但子类不受此限制，除非子类中也定义特殊属性__slots__，则即可继承父类base class的__slot__，又可加上自己定义的__slots__
#    def __init__(self,name,age):   #self实例变量
#        self.name=name
#        self.age=age
#
#class MiddleSchoolStudents(Students):
#    __slots__=('score')


#class screen(object):
#    def __init__(self,width,height):
#        self.__width=width   #__width相当于私有变量，private，外部不能直接调用call 
#        self.__height=height #___双下划线：修饰变量名，可通过dir()内置函数（built-in function）查看属性时看到
#    
#    @property                #@property装饰器，把对象的方法装饰成属性，外部直接像调用属性一样调用即可，不用call（就是不用加 ( )），相当于定义变量
#    def width(self):
#        return self.__width
#
#    @width.setter            #把函数装饰成属性，@width.setter装饰器由上头这段代码的@property装饰器生成，如果不定义，相当于只读属性，加上这段可以像普通变量一样赋值
#    def width(self,value):
#        self.__width = value
#
#    @property
#    def height(self):
#        return self.__height
#    
#    @height.setter
#    def height(self,value):
#        self.__height = value
#    
#    @property
#    def resolution(self):
#        self.__resolution = self.__width * self.__height
#        return self.__resolution

````````````````````````````````````````````````````
#class myclass(object):      #这两个定义类的方法是等价的
#    a = 1                   #类变量
#    b = 2
    #def __init__(self,a):   
    #    self.a=a            #实例变量

#动态定义一个类，终端中可以这么定义，这里貌似不行`````
fyfclass = type('myclass',(object,),{'a':1,'b':2}) #type是默认的metaclass元类  参考 https://blog.csdn.net/wwx890208/article/details/80644400    验证过程通过交互模式验证，在这里写太麻烦
fyfclass.a


#class x():
#    a='fff'
#    b=2





