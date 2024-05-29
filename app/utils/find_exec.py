import os


DIRS = os.environ["PATH"].split(":")


def find_exec(command):
    for path_dir in DIRS:
        path = os.path.join(path_dir, command)
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    return None
