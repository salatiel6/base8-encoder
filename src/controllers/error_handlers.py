from server import server
from docs import error_model
from .exceptions import NumberLengthError, CodeError

api = server.api


class ErrorHandlers:
    @staticmethod
    @api.errorhandler(NumberLengthError)
    @api.marshal_with(error_model, code=400)
    def handle_invalid_number_length_exception(error):
        return {'message': error.message}, 400

    @staticmethod
    @api.errorhandler(CodeError)
    @api.marshal_with(error_model, code=400)
    def handle_invalid_number_length_exception(error):
        return {'message': error.message}, 400
