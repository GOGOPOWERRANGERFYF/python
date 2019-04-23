'''
object oriented progamming 面向对象编程，是一种程序设计思想
在python中，所有数据类型都可以视为对象，当然也可以自定义对象，自定义的数据类型就是面向
对象中的类(class)
class类的变量variable和函数function   (blueprint蓝图)
object对象的属性attribute和方法method
'''
# int   float   string  boolean这些数据类型并不能表示一个学生，因此自定义一个学生数据类型，也就类class
class Students:   #类的名称开头字母大写，一般遵循驼峰命名，只是约定俗成的规定，并非强制性，驼峰命名比如：MyName
    #初始化函数function
    def __init__(self,name,age,score):   #self参数传入对象名，name，age，score也在实例化时传入   （构造函数）
        self.name = name              #比如student1.name = name = 'fyf'
        self.age = age
        self.score = score

    def level(self):
        if self.score >= 90:
            print('优等生')
        elif self.score >= 60:
            print('及格万岁！')
        else:
            print('不读书，上课玩手机！')


#class A():
#    a = 'x'
#    def __init__(self): #__XX__  特殊方法（函数）   __XX私有成员，相当于其他语言的private，可以私有变量和私有方法（函数function），外部不能调用，只能内部调用，私有变量也可以通过内部函数读取而让外部间接调用
#        self.a = 'y'
#
#
#instance = A()               #加括号自动执行__init__(self)    这个为实例化
#print(instance.a)
#
#notinstance = A              #不加括号不执行__init__(self)   这个不是实例化 
#print(notinstance.a)         #没有实例化call调用__init__(self)      注释调类中的   a='x'   后，运行会报错提示类 A没有属性attribute










