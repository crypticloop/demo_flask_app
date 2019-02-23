from flask import Flask, redirect, url_for
from flask_dance.consumer import OAuth2ConsumerBlueprint
app = Flask(__name__)

splitwise_blueprint = OAuth2ConsumerBlueprint(
    "splitwise", __name__,
    client_id="ZLdQXRHBV3yfp4cztKLiRxItwdiA3ZEHG0e7AbAO",
    client_secret="5OukC1OWgdoUexE2AUEnblr0kOlU7HZg0MM0wvFm",
    base_url="https://www.splitwise.com/api/v3.0",
    token_url="https://secure.splitwise.com/oauth/token",
    authorization_url="https://secure.splitwise.com/oauth/authorize",
)
app.register_blueprint(splitwise_blueprint, url_prefix="/well_done")

@app.route("/")
def hello():
    if not splitwise_blueprint.session.authorized:
        return redirect(url_for(splitwise_blueprint.login))
    return splitwise_blueprint.session.get("/api/v3.0/get_current_user").content


@app.route("/well_done")
def well_done():
    return "I think we're in!"

if (__name__ == '__main__'):
    app.run(debug=True)
