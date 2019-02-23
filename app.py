from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
app = Flask(__name__)
app.config['SECRET_KEY'] = "thisissupposedtobeasecret"

github_blueprint = make_github_blueprint(client_id='8fba127a89b42169c9e1', client_secret ='e0fe3ca09b53ad63576e45e7c8296edaf6369d4f')

app.register_blueprint(github_blueprint, url_prefix='/github')

@app.route("/")
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        return "You're not meant to be here"

@app.route("/github")
def github_authorised():
    return "You made it!"


if (__name__ == '__main__'):
    app.run(debug=True)
