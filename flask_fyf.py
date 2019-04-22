from flask import Flask,render_template,url_for,redirect,request,flash

app = Flask(__name__)
app.secret_key = 'fyfsecretkey'   #传输某些数据需要加密，密钥，例如返回flash()闪现消息就需要加密

'''
URL   '/'        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
@app.route('/')  #带参数的装饰器
def index():      #视图函数views
    #class student(object):   #class类继承object有更多高级特性，不继承则只有两三个高级特性
    #    name = 'sss'
    #    age = 18
    #s = student
    list1 = ['fyf',22,True]
    list2 = [1,2,3,4,5,6,7,8,9]
    list3 = ['a','b','c','d','e','f','g']
    str1 = 'abcdefg'
    context = {                                   #定义一个字典
        'name' : '诸葛亮',                           #key-value键值对,key必须为string字符串
        'age' : 100,
        'profile' : '诸葛亮散文代表作有《出师表》《诫子书》等'
    }
    date = '上午 10:35'
    return render_template('index.html',context=context,date=date,list1=list1,list2=list2,list3=list3,str1=str1)#**关键字参数，传入参数后自动封装成一个字典dictionary，*关键字参数，传入元组tuple，传入参数后前端直接调用就行了，框架已经帮处理好了，不用担心数据类型的问题I



'''
URL   '/article/<id>'     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
@app.route('/article/<id>')       #带参数的装饰器，URL的一部分标记为<variable_name>就可以在
def url_id(id):                   #URL中添加变量,标记的部分会作为关键字参数传递给函数
    print(url_for('url_id',id='aaa')) #URL反转：根据视图函数名称得到URL
    return '这就是你的参数： %s' %id



'''
URL    '/bilibili'    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
@app.route('/bilibili')
def redirect_blibli():
    # return redirect(url_for('login'))
    return redirect('https://www.bilibili.com') #重定向redirect，可用于需要登录才能访问的页面，if判断，没有登录的话返回登录页面


'''
URL    '/login'     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
@app.route('/login',methods=['GET','POST']) #第二个parameter形参是关键字参数，查看源码，传入methods请求方式的列表
def web_login():
    if request.method == 'POST':
        username = request.form.get("username")             #request对象的form属性get方法，获取表单input的元素，通过input label标签的name属性获取
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        email = request.form.get("email")
        print(username)
        print(password1)
        print(password2)
        print(email)
        if not all([username,password1,password2,email]):   #built-in内置函数，call()，判断可迭代对象iterable，包含 0，空   ' '，None，False时返回False，其余为True
            #return '输入不完整'
            flash('输入不完整')
            return render_template('login.html')
        #return '注册成功'
        else:
            flash('注册成功')
            return render_template('login.html')
    else:                                       #request.method == 'GET'
        return render_template('login.html')
    
    #user = {
    #    'username':'王麻子',
    #    'age':18
    #}
    #return render_template('login.html',user=user)
    #if fyf_login == '1':
    #    return render_template('login.html',user=user)
    #else:
    #    return render_template('login.html')

#@app.route('/navigation')
#def navigation():
#    return render_template('navigation.html')

@app.route('/include')
def navigation():
    return render_template('include.html')

@app.route('/extends')    #base.html继承了navigation.html
def extends_index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)




