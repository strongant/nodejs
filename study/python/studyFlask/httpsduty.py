# _*_coding: UTF-8_*_
from flask import Flask,url_for, request, render_template,Markup

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        print 'execute login()'
    else:
        print 'show login form'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

with app.test_request_context('hello',method='POST'):
    #生成css的restful地址
    '''
    print 'css:%s'%url_for('static',filename='style.css')
    print Markup('<strong>Hello %s!</strong>')%'<blink>hacker</blink>'
    print Markup.escape('<blink>hacker</blink>')
    print Markup('<em>Marked up </em>&raquo;HTML').striptags()
    '''
    assert request.path
    assert request.method


if __name__ == '__main__':
    app.run('0.0.0.0')
    app.run(debug=True)
