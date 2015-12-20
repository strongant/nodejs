# _*_coding: UTF-8_*_
from flask import Flask,request,make_response, redirect,render_template, url_for

app = Flask(__name__)


@app.route('/cookie',methods=['POST','GET'])
def cookie(name=None):
    name = request.cookies.get('username')
    name = request.form['username']
    app.logger.debug('name:',name)
    request.__setattr__('name',name)
    return render_template('hello.html',name = name)


@app.route('/login',methods=['GET','POST'])
def login():
    app.logger.warning('login()')
    return render_template('login.html')

@app.route('/')
def index():
    app.logger.error('url_for',url_for('login'))
    return redirect(url_for('login'))

'''
#存储cookie
@app.route('/')
def index():
    resp = make_response(render_template('login.html'))
    resp.set_cookie('username','the useranme')
    return resp
'''


if __name__ == '__main__':
    app.run('0.0.0.0')
    app.run(debug=True)

