from flask import Flask, redirect, url_for
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return "Back to the start"


@app.route("/well_done")
def well_done():
    return "I think we're in!"

if (__name__ == '__main__'):
    app.run(debug=True)
