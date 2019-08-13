#! /usr/bin/env python3

# working from
# * http://inventwithpython.com/blog/2012/04/06/stop-using-print-for-debugging-a-5-minute-quickstart-guide-to-pythons-logging-module/
# * https://docs.python.org/3/howto/logging.html#a-simple-example
# * Eric's code ideas: https://gist.github.com/eric-s-s/11e08dbc38891fa3d0eba5396703afc6

import logging
from os import getlogin, path
import platform
from pwd import getpwnam
from sys import stderr

# Can this be called from __init__.py? So it's running before main()...
def log_config():
    """Unique name by machine and user.
    OS X: ~/Library/Logs/<machine-name>_<username>.log

    :return: log file name
    """

    # https://docs.python.org/3/howto/logging-cookbook.html#logging-to-multiple-destinations to use instead
    # of print to stderr.

    home = getpwnam(getlogin()).pw_dir
    machine_user = str.split(platform.uname()[1], ".local")[0] + "_" + getlogin()

    log_file_path = path.join(home, "Library/Logs/")  # MacOS location
    if not path.exists(log_file_path):
        log_file_path = home  # Linux location

    log_file = path.join(log_file_path, machine_user + ".log")

    # basicConfig below will raise an exception - fix that

    logging.basicConfig(
        filename=log_file,
        format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO,
    )
    return log_file


def log_critical(msg: str, indent: str = "\n    "):
    print(indent + msg, sep="", file=stderr)
    logging.critical(msg)


def log_debug(msg: str, indent: str = "\n    "):
    print(indent + msg, sep="", file=stderr)
    logging.debug(msg)


def log_end():
    # https://stackoverflow.com/questions/26017073/how-to-get-filename-from-a-python-logger
    f = logging.getLogger().handlers[0].baseFilename
    logging.info(": End")
    logging.shutdown()
    print("Actions recorded in ", f, ".", sep="", file=stderr)


def log_error(msg: str, indent: str = "\n    "):
    print(indent + msg, sep="", file=stderr)
    logging.error(msg)


def log_info(msg: str, indent: str = "\n    "):
    print(indent + msg, sep="", file=stderr)
    logging.info(msg)


# path.abspath(__file__) or figure out who's calling dglogger, think there is a feature for that
def log_start():
    logging.info(": Start")


def log_warning(msg: str, indent: str = "\n    "):
    print(indent + msg, sep="", file=stderr)
    logging.warning(msg)


#
# Test
# Figure out Python unit testing
#
def test():
    log_config()
    log_start()
    log_info("Testing log_info()")
    log_warning("Testing log_warning()")
    log_error("Testing log_error()")
    log_debug("Testing log_debug()")
    log_end()
