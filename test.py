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

def outter(msg='haha'):
    def inner(x):
        print(msg + x)
    return inner

f = outter()
print(f)
#print(f.__name__)
#print(f('hehe'))