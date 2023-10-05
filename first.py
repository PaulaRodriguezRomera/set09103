from flask import Flask,flash, url_for, request, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3 yX R~XHH!jmN]LWX/,? RT'

@app.route('/')
def index():
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

@app.route('/jinga/<name>')
def template(name=None):
    user = {'name' : name}
    return render_template('conditional.html', user=user)

@app.route('/users/')
def users():
    names = ['simon', 'thomas', 'paula', 'jaime', 'sylvester']
    return render_template('loops.html', names=names)

@app.route('/inherits/')
def inherits():
    return render_template('base.html')

@app.route('/inherits/one/')
def inherits_one():
    return render_template('inherits1.html')

@app.route('/inherits/two/')
def inherits_two():
    return render_template('inherits2.html')

@app.route('/session/write/<name>/')
def write(name=None):
    session['name'] = name
    return 'Wrote %s into "name" key of session' % name
@app.route('/session/read')
def read():
    try:
        if(session['name']):
            return str(session['name'])
    except KeyError:
        pass
    return "No session variable set for 'name' key"

@app.route('/session/remove/')
def remove():
    session.pop('name', None)
    return "Removed key 'name' from session"


@app.route('/login/')
@app.route('/login/<message>')
def login(message=None):
    if (message != None):
        flash(message)
    else:
        flash(u'A default message')
    return redirect(url_for('index'))

@app.route('/style/')
def style():
    return render_template('boostrap_demo.html'), 200