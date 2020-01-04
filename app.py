from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3
from sqlite3 import Error


con1 = sqlite3.connect('aditi_posts.db', check_same_thread=False)
cursorObj = con1.cursor()


@app.route('/index', methods=['GET', 'POST'])
def render_homepage():
    if request.method == "POST":
        val = validate_login()
        if val == False:
            return "Username and password did not match."

    return render_template('index.html')


@app.route('/posts')
def render_posts():
    cursorObj.execute('select * from posts')
    rows = cursorObj.fetchall()

    return render_template('posts.html', result=rows)

@app.route('/login')
def render_login():
    return render_template('login.html')

def validate_login():
    
    q = "select * from users where username = '" \
    + str(request.form['username']) + "'"
    
    print(q)
    cursorObj.execute(q)
    rows = cursorObj.fetchall()
    pwd = rows[0][2]

    if pwd != request.form['password']:
        return False
    
    return True






if __name__ == "__main__":
    app.run(debug=True)