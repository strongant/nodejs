# _*_coding: UTF-8_*_
import os
import sqlite3
from flask import Flask,session,request,g,redirect,url_for,abort,render_template,flash

app = Flask(__name__)

#设置session secret_key
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'



def connect_db():
    """Connects to the specific database"""
    connect = sqlite3.connect('/home/bwh/tmp/flaskr.db')
    return connect

def init_db():
        connect = connect_db()
        with app.open_resource('schema.sql',mode='r') as f:
            connect.cursor().executescript(f.read())
        connect.commit()
        return connect

@app.route('/')
def show_entries():
    #初始化数据库
    cur = connect_db()
    cur = cur.execute('select title,text from entries order by id desc')
    entries = [dict(title=row[0],text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html',entries=entries)

@app.route('/add',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    #向数据库进行插入值
    connect = connect_db()
    connect.execute('insert into entries (title,text) values(?,?)',[request.form['title'],request.form['text']])
    connect.commit()
    flash('New entry was successfully posted')
    print 'url:',url_for('show_entries')
    #重定向到根目录
    return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method =='POST':
        if request.form['username']!="admin":
            error = 'Invalid username'
        elif request.form['password']!="admin":
            error = 'INvalid password'
        else:
            session['logged_in'] = True
            #g.__setattr__('logged_in',request.form['username'])
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html',error=error)

@app.route('/logout')
def logout():
    g.__setattr__('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
