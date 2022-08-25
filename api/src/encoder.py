from .config import Config


class Encoder:

    def __init__(self, number: int):
        self._number = number

    def encode(self):
        config = Config()
        encoded = ""

        module_list = []

        while self._number >= 32:
            module_list.append(self._number % 32)
            self._number //= 32

        module_list.append(self._number)

        module_list = module_list[::-1]

        for i in module_list:
            encoded += config.cipher[i]

        while len(encoded) < 6:
            encoded += "="

        return encoded
