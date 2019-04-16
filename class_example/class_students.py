'''
object oriented progamming 面向对象编程，是一种程序设计思想
在python中，所有数据类型都可以视为对象，当然也可以自定义对象，自定义的数据类型就是面向
对象中的类(class)
'''
# int   float   string  boolean这些数据类型并不能表示一个学生，因此自定义一个学生数据类型，也就类class
class Students:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score