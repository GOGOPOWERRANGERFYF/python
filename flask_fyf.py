from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')  #带参数的装饰器
def index():
    return render_template('index.html')

@app.route('/article/<id>')       #url传参数，URL的一部分标记为<variable_name>就可以在
def url_id(id):                   #URL中添加变量,标记的部分会作为关键字参数传递给函数
    return '这就是你的参数： %s' %id

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

