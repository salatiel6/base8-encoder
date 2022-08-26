class NumberLengthError(Exception):
    def __init__(self):
        self.message = "The number must have a maximun of 8 characters"


class CodeError(Exception):
    def __init__(self):
        self.message = "Invalid code"
