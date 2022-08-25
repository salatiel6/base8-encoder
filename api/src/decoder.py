from .config import Config

class Decoder:

    def __init__(self, encoded: str):
        self._encoded = encoded

    def decode(self):
        config = Config()
        reversed_encoded = self._encoded.split("=")[0][::-1]

        key_list = list(config.cipher.keys())
        value_list = list(config.cipher.values())

        values = []
        for i in reversed_encoded:
            values.append(key_list[value_list.index(i)])

        decoded = 0
        for i, number in enumerate(values):
            decoded += number * (pow(32, i))

        return decoded
