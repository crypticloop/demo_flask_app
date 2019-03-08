from requests_oauthlib import OAuth2Session
import requests
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os
from splitwise import Splitwise

app = Flask(__name__)

sObj = Splitwise("ZLdQXRHBV3yfp4cztKLiRxItwdiA3ZEHG0e7AbAO","5OukC1OWgdoUexE2AUEnblr0kOlU7HZg0MM0wvFm")
url, secret = sObj.getAuthorizeURL()



@app.route("/")
def demo():
    return redirect(url)

@app.route("/callback")
def callback():
    oauth_token    = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')

    session['secret']=secret
    access_token = sObj.getAccessToken(oauth_token,session['secret'],oauth_verifier)

    session['access_token'] = access_token

    sObj.setAccessToken(session['access_token'])

    cheese = sObj.getCurrentUser()

    return cheese.getFirstName()







if __name__ == "__main__":
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
    app.secret_key = os.urandom(24)
    app.run(debug=True)
