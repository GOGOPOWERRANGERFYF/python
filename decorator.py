'''
decorator 装饰器,闭包函数的一种特例，内部函数调用外部函数的参数，该参数为函数
'''

'''
# 1.
def add_candle(cake):
    def insert_candle():
        return cake() + " candle"
    return insert_candle

def make_cake():
    return "cake"

f = add_candle(make_cake)
print(f())
'''

'''
# 2.
def add_candle(cake):
    def insert_candle():
        return cake() + " candle"
    return insert_candle

def make_cake():
    return "cake"

make_cake = add_candle(make_cake)

print(make_cake.__name__)
print(make_cake())
'''
'''
3.
def add_candle(cake):              #cake为函数名function
    def insert_candle():          #内部函数调用外部函数的参数，这个参数是一个函数，所以是特殊的闭包函数
        return cake() + " candle"  #cake()函数调用call
    return insert_candle

@add_candle                       #make_cake函数作为参数传入add_candle函数中
def make_cake():
    return "cake"

print(make_cake.__name__)
print(make_cake())
'''
'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
'''
带参数的装饰器decorator
'''

#def cake_name(x): #装饰器外再套一层函数,x参数可以传入闭包函数内
#    def add_candle(f):  
#        def insert_candle():
#            print('%s ' %x + '%s add candle :)' %f())
#        return insert_candle
#    return add_candle #x传入后,中间为定义闭包函数enclosing function,而且是装饰器decorator,这一步返回其实就是返回decorator
#
##作用：把数据x封装起来，x是全局变量的话修改后也会影响其它调用该变量的函数
#@cake_name('Yes, This is alibaba') #传入参数x,返回add_candle，等于@add_candle = add_candle(make_cake)
#def make_cake():                   
#    return 'cake'
#
#make_cake()

def cake_name(x): #装饰器外再套一层函数,x参数可以传入闭包函数内
    def add_candle(f):  
        def insert_candle():
            print(x)
            print(f(x))
        return insert_candle
    return add_candle #(1)x传入后,中间为定义闭包函数enclosing function,而且是装饰器decorator,这一步返回其实就是返回decorator

#作用：把数据x封装起来，x是全局变量的话修改后也会影响其它调用该变量的函数
@cake_name('Yes, This is alibaba') #(2)传入参数x,返回add_candle，等于@add_candle = add_candle(make_cake)=make_cake()
def make_cake(x):                   
    return '被装饰函数接收到了带参数的装饰器的传入参数：%s' %x

make_cake()



