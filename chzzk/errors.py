class ChzzkError(Exception):
    def __init__(self, message: str):
        self.message = message


class ChzzkHTTPError(ChzzkError):
    def __init__(self, message: str, code: int):
        super().__init__(message)

        self.code = code
