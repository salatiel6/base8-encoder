import re

from flask_restx import Resource
from .encoder import Encoder
from .decoder import Decoder
from server import server
from docs import encode_model, decode_model, error_model
from .exceptions import NumberLengthError, CodeError
from .error_handlers import ErrorHandlers

app, api = server.app, server.api
app.config["RESTX_MASK_SWAGGER"] = False
error_handlers = ErrorHandlers


@api.route("/encode/<int:number>", doc={
    "description": "Receives a number and encode it"
})
@api.param("number", "The number to be encoded")
class Encode(Resource):
    @api.response(200, "Success", encode_model)
    @api.response(400, "Number Length Error", error_model)
    def get(self, number):
        if len(str(number)) > 8:
            raise NumberLengthError()

        encoder = Encoder(number)
        encoded = encoder.encode()

        return {
            "encoded": encoded
        }, 200


@api.route("/decode/<string:encoded>", doc={
    "description": "Receives the encoded number and decode "
                   "it back to its original content"
})
@api.param(
    "encoded", "The previous encoded number that is going to be decoded"
)
class Decode(Resource):
    @api.response(200, "Success", decode_model)
    @api.response(400, "Code Error", error_model)
    def get(self, encoded):
        if not re.findall("^[A-V0-9=]{6}$", encoded):  # noqa
            raise CodeError()

        decoder = Decoder(encoded)
        decoded = decoder.decode()

        return {
            "decoded": decoded
        }, 200
