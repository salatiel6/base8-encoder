from flask_restx import fields
from shape_challenge.src.server import server

encode_model = server.api.model(
    "encode_model", {
        "encoded": fields.String(
            description="The encoded value returned from the input"
        )
    }
)

decode_model = server.api.model(
    "decode_model", {
        "decoded": fields.Integer(
            description="The decoded value returned from the input"
        )
    }
)
