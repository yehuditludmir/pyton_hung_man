class inputNumInsteadOfaString(Exception):
    """Custom exception for number instead of a string"""

    def __init__(self, message="You entered a number instead of a string"):
        self.message = message
        super().__init__(self.message)

class inputCharInsteadOfaNumber(Exception):
    """Custom exception for char instead of a number"""

    def __init__(self, message="You entered a char instead of a number"):
        self.message = message
        super().__init__(self.message)

class wrongOption(Exception):
    """Custom exception for wrong option"""

    def __init__(self, message="You entered wrong option"):
        self.message = message
        super().__init__(self.message)