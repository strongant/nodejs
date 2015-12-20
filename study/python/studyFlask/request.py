# _*_coding: UTF-8_*_
__author__ = 'bwh'
from flask import Flask,request, render_template

app = Flask(__name__)


def log_the_user_In(param):
    pass

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dologin',methods=['POST','GET'])
def dologin():
    error = None
    if request.method=='POST':
        print request.form['username']
        print request.form['password']
        if valid_login(request.form['username'],request.form['password']):
            return log_the_user_In(request.form['username'])
        else:
            error = "Invalid username or password"
    return render_template('../login.html',error=error)

def valid_login(username,password):
   return True

if __name__ == '__main__':
    app.run('0.0.0.0')
    app.run(debug=True)
