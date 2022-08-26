import re

from flask_restx import Resource, fields
from .encoder import Encoder
from .decoder import Decoder
from shape_challenge.src.server import server
from shape_challenge.src.docs import encode_model, decode_model

app, api = server.app, server.api


@api.route("/encode/<number>")
class Encode(Resource):
    @api.marshal_with(encode_model, code=200)
    def get(self, number):
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


@api.route("/decode/<encoded>")
class Decode(Resource):
    @api.marshal_with(decode_model, code=200)
    def get(self, encoded):
        if not re.findall("^[A-V0-9=]{6}$", encoded):
            return {
                "message": "Invalid code"
            }, 400

        decoder = Decoder(encoded)
        decoded = decoder.decode()

        return {
            "decoded": decoded
        }, 200
