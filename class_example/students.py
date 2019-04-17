from class_students import Students    #从class_students文件导入Students类(class)

#object is  an instance on the class 对象object是一个类class的实例instance
student1 = Students('fyf',18,100) #这个类就像一个模板它定义了一个学生是什么,实例化一个对象
student2 = Students('fxf',20,95) 

print(student1)
print(student1.name)
print(student1.age)
print(student1.score)    

