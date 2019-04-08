#导入    flask模块   的   Flask类(class)
from flask import Flask,render_template,request,redirect   #从flask模块module导入Flask 类class

#实例化Flask对象(面向对象编程)
#__name__ 当前模块(moudle) 的名字，__name__ == '__main__'  == 'flask_test'
app = Flask(__name__)

#定义路由及视图函数(function)
#flask定义路由通过装饰器(decorator)来实现
#methods(请求方式) 参数默认GET
@app.route('/',methods=['GET','POST'])   # 1, 第一步执行app.route('/')  返回inner    2. 第二步执行 inner(index)
def index():
    if request.method == "GET":  #request对象的作用是与客户端交互
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('password')
        if user == 'fyf' and pwd == '123456':
            return redirect('https://www.bilibili.com')
        return render_template('login.html',error='密码或用户名错误')
    
    
    #return '我是网站！见过这么屌的网站吗！'

#<>URL添加变量部分,<>作为命名参数传递到函数
@app.route('/school/<int:student_id>')
def show_student_id(student_id):
    return 'student_id %d' % student_id

if __name__ == '__main__':
    #监听用户请求
    app.run(host='0.0.0.0')
    #如果有用户请求到来，则执行app的__call__方法
    #app.__call__


