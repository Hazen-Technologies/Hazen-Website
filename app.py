from flask import Flask, render_template, g ,  request

import sqlite3
app = Flask(__name__)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404
    
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/terms-and-conditions")
def terms():
    return render_template('terms-conditions.html')


@app.route("/explore")
def explore():
 return render_template('explore.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/games")
def games():
    return render_template('games.html')

@app.route("/report")
def report():
    return render_template('report.html')


@app.route("/thanks")
def thanks():
    return render_template('thanks.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/cookie-policy")
def cookiepolicy():
    return render_template('cookie-policy.html')



@app.route("/news")
def news():
    dbg = sqlite3.connect('database.db')
    dbg.row_factory = sqlite3.Row
    posts = dbg.execute('SELECT * FROM posts').fetchall()
    dbg.close()
    return render_template('news.html', posts=posts)

@app.route("/news/posts/2022/welcome")
def posts():
    dbg = sqlite3.connect('database.db')
    dbg.row_factory = sqlite3.Row
    posts = dbg.execute('SELECT * FROM posts').fetchall()
    dbg.close()
    return render_template('welcome-posts.html', posts=posts)
