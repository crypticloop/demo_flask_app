from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
app = Flask(__name__)

@app.route("/")
def hello():
    return "You made it"

if (__name__ == '__main__'):
    app.run(debug=True)
