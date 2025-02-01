import sys

from urllib.error import URLError
from interface import Text


def catch_error(error_type=Exception, error=None) -> None:
    """
    Handle errors to avoid the application to crash with long error messages, and instead show a nicer and simpler
    error message.
    :param error_type: The type of the error (KeyboardInterrupt, ...).
    :param error: The actual error if it's none of the previous error type.
    """
    if error_type == KeyboardInterrupt:
        print(f"{Text.RED}\n\U0001F6D1 Game stopped as requested.{Text.END}\n\n")
    else:
        print(f"{Text.RED}\n\U0001F6A8 An error occurred...\n>>> {error}{Text.END}\n\n")

    sys.exit(0)
