from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def root():
    return 'Default root'

@app.route('/hello/')
def hello():
    return 'Hello You!'

@app.route('/goodbye/')
def goodbye():
    return 'Goodbye You!'

@app.errorhandler(404)
def page_not_found(error):
    return "Could not find the page you requested. Please try again!", 404

@app.route('/static-example/img')
def static_example_img():
    start = '<img src="'
    url = url_for('static', filename='vmask.jpg')
    end = '">'
    return start+url+end, 200