from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Why Hello %s!\n' % username

@app.route('/perfectvips') # dynamic route
def perfectvips():
    return 'hello from perfectvips'


if __name__ == '__main__':
    app.run()