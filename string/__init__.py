from .pyrogRam import *


def __list_all_string():

    from os.path import dirname, basename, isfile

    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")

    all_string = [

        basename(f)[:-3] for f in mod_paths

        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")

    ]

    return all_string

ALL_STRING = sorted(__list_all_string())

LOGS.info("String to load: %s", str(ALL_STRING))

__all__ = ALL_MODULES + ["ALL_STRING"]
