import os
import sys


def get_resource(resource) -> str:
    """
    Get the correct path of a ressource, because the path is different from local to the final executable.
    :param resource: Only the game's music for this project, but it can be any file type.
    :return: The correct path of the resource depending on if it's local or if it's the final executable.
    """
    try:
        base_path = sys._MEIPASS
    except (Exception,):
        base_path = os.path.abspath(".")
    return os.path.join(base_path, "./res/") + "/" + resource
