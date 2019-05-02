'''
@property 装饰器decorator   property是一个内置类built-in class,函数function和类class都可以做装饰器
'''

#用@property装饰器
class screen(object):
    def __init__(self,width,height):
        self.__width=width   #__width相当于私有变量，private，外部不能直接调用call 
        self.__height=height #___双下划线：修饰变量名，可通过dir()内置函数（built-in function）查看属性时看到
    
    @property                #@property装饰器，把对象的方法装饰成属性，外部直接像调用属性一样调用即可，不用call（就是不用加 ( )），相当于定义变量
    def width(self):
        return self.__width

    @width.setter            #把函数装饰成属性，@width.setter装饰器由上头这段代码的@property装饰器生成，如果不定义，相当于只读属性，加上这段可以像普通变量一样赋值
    def width(self,value):
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,value):
        self.__height = value
    
    @property
    def resolution(self):
        self.__resolution = self.__width * self.__height
        return self.__resolution


#直接用property类的例子
class person(object):
    def __init__(self,name):
        self.name=name
    
    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name=name
        return self.name

    personname = property(get_name,set_name) #实例化property类，property数据类型，类包含属性和方法，oop面向对象编成的概念











