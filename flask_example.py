# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from layer import generate_identity_token

app = Flask(__name__)


@app.route("/identity_token", methods=['POST'])
def get_identity_token():
    user_id = request.form.get('user_id', '')
    nonce = request.form.get('nonce', '')

    if not (user_id and nonce):
        return "Invalid Request."

    # Create the token
    identityToken = generate_identity_token(user_id, nonce)

    # Return our token with a JSON Content-Type
    return jsonify({"identity_token": identityToken})

if __name__ == "__main__":
    app.run()
