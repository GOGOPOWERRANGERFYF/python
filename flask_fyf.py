from flask import Flask,render_template,url_for,redirect,request,flash
#如果__init__.py文件为空的话，必须要 import   flask_wtf.form.FlaskForm或者from    flask_wtf.form   import    FlaskForm 这样导入import。但__init__.py不为空，查看源码后，采用下面的导入方式
from flask_wtf import FlaskForm    #从flask_wtf组件(包package)中导入form.py模块(module)的FlaskForm类
from wtforms import StringField,PasswordField,SubmitField  #从wtforms组件(包package) 中导入 支持多个web框架，主要用于用户请求数据进行验证 ，Field字段
from wtforms.validators import DataRequired,EqualTo,Email  #从wtforms包(package)的validators模块(module)   导入import    DataRequired类(class)等
#从wtforms包的__init__.py文件可知，已经初始化导入了validator模块，所以是可用   import wtforms.DataRequired这样导入的，但导入多个类没有上面的方式方便
#重点：主要要看__init__.py文件（如果不为空的话）。导入方式很多种，无法一一列举，具体情况具体分析，看源码，看__init__.py文件 
#__init__.py为空的话，import  package.(subpackage如果有).module.class(or variable,function)    或者   from   import也可以，总而言之就是像绝对路径的概念

app = Flask(__name__)
app.secret_key = 'fyfsecretkey'   #传输某些数据需要加密，密钥，例如返回flash()闪现消息就需要加密

#URL   '/'        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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


#URL   '/article/<id>'     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/article/<id>')       #带参数的装饰器，URL的一部分标记为<variable_name>就可以在
def url_id(id):                   #URL中添加变量,标记的部分会作为关键字参数传递给函数
    print(url_for('url_id',id='aaa')) #URL反转：根据视图函数名称得到URL
    return '这就是你的参数： %s' %id


#URL    '/bilibili'    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/bilibili')
def redirect_blibli():
    # return redirect(url_for('login'))
    return redirect('https://www.bilibili.com') #重定向redirect，可用于需要登录才能访问的页面，if判断，没有登录的话返回登录页面


#URL    '/login'     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/include')     #导入引用页面
def navigation():
    return render_template('include.html')

@app.route('/extends')    #base.html继承了navigation.html
def extends_index():
    return render_template('extends.html')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class RegisterForm(FlaskForm):             #自定义一个表单类，继承(inherit)  FlaskForm类   相当于把FlaskForm类的定义代码复制进RegisterForm类中去，查看FlaskForm类源码是有构建函数__init__(self)的
    username = StringField('用户名：',validators=[DataRequired(message='没有输入用户名')])       #实例化username 对象(object) ，查看class StringField源码可知第一个位置parament参数为label，以下同理  
    password1 = PasswordField('密码：',validators=[DataRequired(message='没有输入密码')])
    password2 = PasswordField('确认密码：',validators=[DataRequired(message='请输入确认密码'),EqualTo('password1',message='两次输入密码不同')])  #查看源码可知EqualTo的fieldname参数为字符串string
    email = StringField('邮箱：',validators=[DataRequired(message='请输入邮箱'),Email(message='邮箱格式不正确')])
    submit = SubmitField('注册')

@app.route('/form',methods=['GET','POST'])
def register_web_form():
    registerform = RegisterForm() #实例化对象 form，实例化object 要加（），加（） 才会call调用__init__( )    不加括号只是类对象，不是实例化instance，看FlaskForm的源码可知必须实例化，否则不会执行FlaskForm类的__init__(self)函数
    if request.method == 'POST':
        username = request.form.get('username')     #request表单请求接收到的字段field传入对象username
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        email = request.form.get('email')
        if registerform.validate_on_submit():
            print(username)
            print(password1)
            print(password2)
            print(email)
            flash('注册成功')
        else:
            flash('注册成功')
    return render_template('form.html',form=registerform)
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#print(app.import_name)
#print(__name__)   #该模块被其它模块导入时，__name__='flask_fyf'，在当前模块__name__ = '__main__'
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)




