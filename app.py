from flask import Flask, render_template
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

@app.route('/')
def home():
    return render_template("index.html")
    
@app.route('/chicken')
def chicken():
    return render_template("chicken.html")

@app.route('/vulture')
def vulture():
    return render_template("vulture.html")

@app.route('/duck')
def duck():
    return render_template("duck.html")

@app.route('/form')
def form():
    return render_template("form.html")

if __name__ == '__main__':
    app.debug = True 
    app.run()