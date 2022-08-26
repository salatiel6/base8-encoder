from flask_restx import fields
from server import server

encode_model = server.api.model(
    "encode_model", {
        "encoded": fields.String(
            description="The encoded value returned from the input"
        )
    }
)

error_model = server.api.model(
    "error_model", {
        "message": fields.String()
    }
)

decode_model = server.api.model(
    "decode_model", {
        "decoded": fields.Integer(
            description="The decoded value returned from the input"
        )
    }
)
