from flask import Flask,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return "this is a index method"

@app.route('/login')
def login():
    return 'this is a login method!'

@app.route('/user/<username>')
def show_user_profile(username):
    #show the user profile for that user
    return 'User %s'%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id,the id is an integer
    return 'Post %d'%post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/user/<username>')
def profile(username):pass


with app.test_request_context():
        print url_for('index')
        print url_for('login')
        print url_for('login',next='/')
        print url_for('profile',username = 'John Doe')


if __name__ == '__main__':
    #start access
    app.run('0.0.0.0')
    app.run(debug=True)



