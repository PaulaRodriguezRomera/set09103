from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# List of words or phrases
words = ["Hello", "World", "Flask", "Python", "Web"]

@app.route('/')
def index():
    # Get the previously generated random word from the session
    random_word = request.args.get('random_word')
    return render_template('index.html', random_word=random_word)

@app.route('/generate_word', methods=['POST'])
def generate_word():
    if request.method == 'POST':
        # Select a random word from the list
        random_word = random.choice(words)
        # Redirect back to the index route with the random_word as a query parameter
        return redirect(url_for('index', random_word=random_word))


