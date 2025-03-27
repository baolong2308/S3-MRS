from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h2> helloworld </h2>"


@app.route('/user/<name>')
def hello_user(name):
    if name == 'Long':
        return redirect(url_for('admin'))
    return f"<h1> hello {name}! </h1>"


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    return f"<h1> blog {blog_id} </h1>"

@app.route('/admin')
def admin():
    return "<h1> Hello, admin! "


if __name__ == "__main__":
    app.run(debug=True)