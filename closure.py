'''
Closure:
    1.Nested function 嵌套函数
    2.Nested function must refer values in enclosing scope 封闭作用域
    3.enclosing function must return nested function
'''

def outer(msg):
    #msg = 'hello'
    def inner():
        print(msg)    #闭包函数先在自身作用域找变量值，没有时往上一层作用域找，函数内没有可找全局变量
    return inner

f = outer('ni hao')
print(f.__name__)
f1 = outer(123)
f1()
# f2 = inner()  错误:外部不能调用闭包函数


def m(x=2):
    def n(y):
        c = x**y
        return c
    return n

r = m()
print(r.__name__)
print(r(9))
print(r(10))

