from requests_oauthlib import OAuth2Session
import requests
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os

app = Flask(__name__)


@app.route("/")
def demo():
    return "REN!"


if __name__ == "__main__":

    app.run(debug=True)
