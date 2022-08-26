import re

from flask_restx import Resource
from .encoder import Encoder
from .decoder import Decoder
from server import server
from docs import encode_model, decode_model
from .exceptions import NumberError, NumberLengthError, CodeError
from .error_handlers import ErrorHandlers

app, api = server.app, server.api
error_handlers = ErrorHandlers


@api.route("/encode/<number>")
class Encode(Resource):
    @api.marshal_with(encode_model, code=200)
    def get(self, number):
        if not number.isdigit():
            raise NumberError()

        if len(number) > 8:
            raise NumberLengthError()

        encoder = Encoder(int(number))
        encoded = encoder.encode()

        return {
            "encoded": encoded
        }, 200


@api.route("/decode/<encoded>")
class Decode(Resource):
    @api.marshal_with(decode_model, code=200)
    def get(self, encoded):
        if not re.findall("^[A-V0-9=]{6}$", encoded):  # noqa
            raise CodeError()

        decoder = Decoder(encoded)
        decoded = decoder.decode()

        return {
            "decoded": decoded
        }, 200
