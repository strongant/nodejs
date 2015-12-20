# _*_coding: UTF-8_*_
from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('file.html')

@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method=='POST':
        f = request.files['the_file']
        f.save('/home/bwh/tmp'+f.filename)

if __name__=="__main__":
    app.run('0.0.0.0',debug=True)

