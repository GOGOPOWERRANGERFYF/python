from flask import Flask,render_template,url_for,redirect

app = Flask(__name__)

@app.route('/')  #带参数的装饰器
def index():
    return render_template('index.html')

@app.route('/article/<id>')       #带参数的装饰器，URL的一部分标记为<variable_name>就可以在
def url_id(id):                   #URL中添加变量,标记的部分会作为关键字参数传递给函数
    print(url_for('url_id',id = 'aaa')) #URL反转：根据视图函数名称得到URL
    return '这就是你的参数： %s' %id

@app.route('/bilibili')
def redirect_blibli():
    return redirect('https://www.bilibili.com') #重定向redirect，可用于需要登录才能访问的页面，if判断，没有登录的话返回登录页面

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

