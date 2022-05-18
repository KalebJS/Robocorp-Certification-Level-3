import time
from functools import wraps

from .exceptions import ServerError


def retry_on_server_error(func):
    """
    Decorator to retry a function call if it fails with a ServerError.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for t in range(3):
            try:
                return func(*args, **kwargs)
            except ServerError:
                try_num = t + 1
                seconds_wait = 3 ** try_num
                print("ServerError, retrying in {} seconds (retry {}/3)...".format(seconds_wait, try_num))
                time.sleep(seconds_wait)

        raise ServerError("Server side error")

    return wrapper
