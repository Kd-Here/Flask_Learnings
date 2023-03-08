from markupsafe import escape
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
def hello():
    return 'Hello, World'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<uuid:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {(subpath)}'


# Unique Urls behaviour
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return '<b>The about page</b>'

# ###################
#URL Building :- To build url from knowing the function is also called reversing.
# ###################

from flask import url_for
with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('hello', next='/'))
    print(url_for('show_user_profile', username='kd'))
    print(url_for('about'))
    print(url_for('show_post',post_id=9899))
    print(url_for('static', filename='style.css'))






######################
# Http requests 
######################
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "<h1>Accesing via post</h1>"
    else:
        return "<h1>Accesing via Get</h1>"
    


######################
# Html page rendering
######################

from flask import render_template

@app.route('/Home')
def Home():
    return render_template('home.html')



###############
#Accessing Request Data
# https://flask.palletsprojects.com/en/2.2.x/quickstart/#accessing-request-data
###############