from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def root():
    return 'Default root'

@app.route('/good-morning/')
def good_morning():
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

@app.route("/account/", methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        return "Hello  %s" % name
    else:
        page = '''
        <html><body>
        <form action="" method="post" name="form">
            <label for="name"> Name: </label>
            <input type="text" name="name" id="name"/>
            <input type="submit" name="submit" id="submit"/>
        </form>
        </body><html>'''

        return page

@app.route("/hello/<name>")
def hello(name):
    return "Hello %s" % name

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
    return str(first+second)

@app.route('/parameters/')
def parameters():
    name = request.args.get('name', '')
    if name == '':
        return "no param supplied"
    else:
        return "Hello %s" % name

@app.route("/upload/", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/uploads/file.png')
        return "File uploaded"
    else:
        page = '''
         <html>
         <body>
            <form action="" method="post" name="form" enctype="multipart/form-data">
                <input type="file" name="datafile"/>
                <input type="submit" name="submit" id="submit"/>
            </form>
        </body>
        <html>
        '''

        return page, 200