"""
This file contains stability ai exceptions
"""


class StabilityAIException(Exception):
    """
    Exception raised whenever an error occurs in stability ai sdk.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
