from flask import Flask

app =Flask(__name__) # Creating the app instance

@app.route('/')

def home():
    return "<h1>Welcome to Flask by Nakagga Shanitah from WITI</h1>" \
    "<p>I like coding</p>"

@app.route("/about")
def about():
    return "<h2>Flask basic</h2>"
































