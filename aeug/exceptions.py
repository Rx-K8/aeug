class InsufficientQuestionsError(Exception):
    """Exception raised when the number of questions is insufficient."""
    def __init__(self, message="Number of questions is insufficient."):
        self.message = message
        super().__init__(self.message)
