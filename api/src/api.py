import re

from flask import Flask
from .encoder import Encoder
from .decoder import Decoder

app = Flask(__name__)


@app.route("/")
def index():
    return "Index"


@app.route("/encode/<number>")
def encode(number):
    if not number.isdigit():
        return {
            "message": "Invalid number"
        }, 400

    if len(number) > 8:
        return {
            "message": "The number must have a maximun of 8 characters"
        }, 400

    encoder = Encoder(int(number))
    encoded = encoder.encode()

    return {
        "encoded": encoded
    }, 200


@app.route("/decode/<encoded>")
def decode(encoded):
    if not re.findall("^[A-V0-9=]{6}$", encoded):
        return {
            "message": "Invalid code"
        }, 400

    decoder = Decoder(encoded)
    decoded = decoder.decode()

    return {
        "decoded": decoded
    }, 200