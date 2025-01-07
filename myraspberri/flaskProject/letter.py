from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def welcome_page():
    return render_template('index.html')


@app.route('/login/<name>')
def login_form(name):
    return render_template('login.html', current_name=name)



if __name__ == '__main__':
    app.run(debug=True)