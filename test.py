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

dict = {
    'id':123456789,
    'name':'Li Lei',
    'age': 16
}

def person(**dict):
    return dict

temp1 = person(dict=dict)
print(temp1)
print(temp1['dict'])
print('>>>>>>>>>>>>>>>>>>>')
temp2 = temp1['dict']
print(temp2)
print(temp2['id'])
#temp2 = person(**dict)
#print(temp2['id'])

#if True:
#    print(person(**dict))   #关键字参数，传入0或N个 含参数名的参数（例如：key1='xxx'，key2=18）,函数内部自动封装成一个字典
#    print(person(dict=dict))#运行可看到两者的区别
#else:
#    print('nothing')

