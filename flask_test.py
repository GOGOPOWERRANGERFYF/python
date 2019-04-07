#导入    flask模块   的   Flask类(class)
from flask import Flask

#创建Flask应用程序实例
#__name__ 当前模块(moudle) 的名字，__name__ == '__main__'  == 'flask_test'
app = Flask(__name__)

#定义路由及视图函数(function)
#flask定义路由通过装饰器(decorator)来实现
#methods(请求方式) 参数默认GET
@app.route('/',methods=['GET','POST'])
def a():
    return '我是网站！见过这么屌的网站吗！'

@app.route('/b')
def b():
    return 'b'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

