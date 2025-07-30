from flask import Flask, render_template, url_for
app = Flask(__name__)

# Sample data to simulate a database
posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2025'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2025'
    }
]

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)    # Jinja templating engine allows us to pass variables to HTML templates

@app.route('/about')
def about():
    return render_template('about.html', title='About')