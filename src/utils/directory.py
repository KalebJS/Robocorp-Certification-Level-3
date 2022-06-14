from contextlib import suppress
import os
import shutil


def prepare_directory(directory):
    """
    Prepare a directory for use.
    """
    with suppress(FileNotFoundError):
        shutil.rmtree(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
