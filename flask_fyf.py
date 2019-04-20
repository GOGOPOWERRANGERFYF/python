from flask import Flask,render_template,url_for,redirect

app = Flask(__name__)

@app.route('/')  #带参数的装饰器
def index():
    #class student(object):   #class类继承object有更多高级特性，不继承则只有两三个高级特性
    #    name = 'sss'
    #    age = 18
    #s = student
    list1 = ['fyf',22,True]
    list2 = [1,2,3,4,5,6,7,8,9]
    context = {                                   #定义一个字典
        'name' : '诸葛亮',                           #key-value键值对,key必须为string字符串
        'age' : 100,
        'profile' : '诸葛亮散文代表作有《出师表》《诫子书》等'
    }
    date = '上午 10:35'
    return render_template('index.html',context=context,date=date,list1=list1,list2=list2)#**关键字参数，传入参数后自动封装成一个字典dictionary，*关键字参数，传入元组tuple，传入参数后前端直接调用就行了，框架已经帮处理好了，不用担心数据类型的问题I

@app.route('/article/<id>')       #带参数的装饰器，URL的一部分标记为<variable_name>就可以在
def url_id(id):                   #URL中添加变量,标记的部分会作为关键字参数传递给函数
    print(url_for('url_id',id = 'aaa')) #URL反转：根据视图函数名称得到URL
    return '这就是你的参数： %s' %id

@app.route('/bilibili')
def redirect_blibli():
    # return redirect(url_for('login'))
    return redirect('https://www.bilibili.com') #重定向redirect，可用于需要登录才能访问的页面，if判断，没有登录的话返回登录页面

@app.route('/login/<fyf_login>')
def web_login(fyf_login):
    user = {
        'username':'王麻子',
        'age':18
    }
    if fyf_login == '1':
        return render_template('login.html',user=user)
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

