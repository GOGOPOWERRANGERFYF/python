from class_students import Students   #从class_students模块（class_students.py）导入Students类

'''
class inheritance   类的继承
'''

#意思是HandsomeStudents继承Students类
class HandsomeStudents(Students):      #驼峰命名，约定俗成，并非强制:

#    继承就相当于把 Students类中的这段代码复制过来  >>>>>>>>>>>>>>>>>>>>>>>>> 
   #def __init__(self,name,age,score):  
   #     self.name = name              
   #     self.age = age
   #     self.score = score

   # def level(self):
   #     if self.score >= 90:
   #         print('优等生')
   #     elif self.score >= 60:
   #         print('及格万岁！')
   #     else:
   #         print('不读书，上课玩手机！')
#继承   inheritance   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>             
    
    def handsome(self):
        print('Yes, very handsome')

handsomestudent1 = HandsomeStudents('fyfhandsome',18,99)   #HandsomeStudents继承Students类，所以实例化HandsomeStudents类时跟父类一样要传入三个paraments参数
handsomestudent1.level()       #对象handsomestudent1可调用Students类中的方法function（函数） 
handsomestudent1.handsome()    #HandsomeStudents新增加的方法（新定义的函数function）




