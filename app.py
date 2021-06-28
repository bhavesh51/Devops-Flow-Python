from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/devops/')
def hello_devops():
    return 'Hello from devops!\n'

@app.route('/about/')
def about():
    return 'about us page\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Why Hello %s!\n' % username

@app.route('/perfectvips') # dynamic route
def perfectvips():
    return 'hello from perfectvips'

@app.route('/city') # dynamic route
def city():
    return 'call from city method'

@app.route('/city1') # dynamic route
def city1():
    return 'call from city1 method'

if __name__ == '__main__':
    app.run()