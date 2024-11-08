from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/profile')
@app.route('/register')
@app.route('/login')
@app.route('/create')
@app.route('/place')
@app.route('/places')
@app.route('/events')
def home():
    return render_template('index.html')
 
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    print(username)
    return render_template('index.html')

@app.route('/event/<eventid>')
def show_event(eventid):
    # show the user profile for that user
    print(eventid)
    return render_template('index.html')

@app.route('/place/<placeid>')
def show_place(placeid):
    # show the user profile for that user
    print(placeid)
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', person=name)

#~ @app.route('/path/<path:subpath>')
#~ def show_subpath(subpath):
    #~ # show the subpath after /path/
    #~ return f'Subpath {escape(subpath)}'
