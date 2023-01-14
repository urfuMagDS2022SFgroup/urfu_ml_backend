class UnsupportedLanguageException(Exception):
    """Exception raised if not Russian or English languages passed."""

    pass


class TimeOutException(Exception):
    """Exception raised when model is not loaded"""

    pass


class CantFindModelException(Exception):
    """Exception raised when cant find model locally or remotely"""

    pass
