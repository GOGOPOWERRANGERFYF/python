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

# 3.
def add_candle(cake):              #cake为函数名function
    def insert_candle():          #内部函数调用外部函数的参数，这个参数是一个函数，所以是特殊的闭包函数
        return cake() + " candle"  #cake()函数调用call
    return insert_candle

@add_candle                       #make_cake函数作为参数传入add_candle函数中
def make_cake():
    return "cake"

print(make_cake.__name__)
print(make_cake())
