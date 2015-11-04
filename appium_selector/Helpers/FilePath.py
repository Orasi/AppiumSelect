import os
MAIN_DIRECTORY = os.path.dirname(os.path.dirname(__file__))
def get_full_path(*path):
    return os.path.join(MAIN_DIRECTORY, *path)