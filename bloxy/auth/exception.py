
class AuthenticationError(Exception):
    
    def __init__(self, res: str, code: int = 200, header: dict | None = None) -> None:
        self.response = res
        self.code = code
        self.header = header
        
        