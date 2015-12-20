# _*_coding: UTF-8_*_
from myflask import app

@app.route('/')
def index():
    return "Hello World"


