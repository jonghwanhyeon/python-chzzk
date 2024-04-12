class ChzzkError(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return str(self.message)


class ChzzkHTTPError(ChzzkError):
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code

    def __str__(self):
        return f"[{self.code}] {self.message}"
