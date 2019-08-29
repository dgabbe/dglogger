#! /usr/bin/env python3

# working from
# * http://inventwithpython.com/blog/2012/04/06/stop-using-print-for-debugging-a-5-minute-quickstart-guide-to-pythons-logging-module/
# * https://docs.python.org/3/howto/logging.html#a-simple-example
# * Eric's code ideas: https://gist.github.com/eric-s-s/11e08dbc38891fa3d0eba5396703afc6
from functools import partial
from logging import (
    basicConfig,
    critical,
    debug,
    error,
    exception,
    Formatter,
    getLogger,
    INFO,
    info,
    Logger,
    shutdown,
    StreamHandler,
    warning,
)
from os import getlogin, path
import platform
from pwd import getpwnam
from sys import stderr


# Conditional formatting possible based on levelname?
# change time to exclude milliseconds
def get_stream_handler() -> StreamHandler:
    # By default goes to stderr
    stream_formatter = Formatter(fmt="    [%(asctime)s] %(levelname)s %(module)s:%(lineno)d %(message)s", datefmt='%H:%M:%S')
    sh = StreamHandler()
    sh.setFormatter(stream_formatter)
    return sh


# Can this be called from __init__.py? So it's running before main()...
def log_config(is_log_file_required=False) -> Logger:
    """Unique name by machine and user.
    OS X: ~/Library/Logs/<machine-name>_<username>.log

    References:
    - https://docs.python.org/3/library/logging.html
    - https://docs.python.org/3/howto/logging-cookbook.html#logging-to-multiple-destinations

    :return: Logger object
    """

    user = getlogin()
    home_dir = getpwnam(user).pw_dir
    machine_user = str.split(platform.uname()[1], ".local")[0] + "_" + user

    log_file_path = path.join(home_dir, "Library/Logs/")  # MacOS location
    if not path.exists(log_file_path):
        log_file_path = home_dir  # Linux location

    log_file_name = path.join(log_file_path, machine_user + ".log")

    try:
        basicConfig(
            filename=log_file_name,
            format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
            level=INFO,
        )
    except (PermissionError, FileNotFoundError):
        exception(f"Could not create log file at: {log_file_name}")
        # Add check for is_required...

    logger = getLogger()
    console_handler = get_stream_handler()
    logger.addHandler(console_handler)
    return logger


def log_critical(msg: str):
    critical(msg)


def log_debug(msg: str):
    debug(msg)


def log_end():
    # https://stackoverflow.com/questions/26017073/how-to-get-filename-from-a-python-logger
    f = getLogger().handlers[0].baseFilename
    info("End")
    shutdown()
    print_err("Actions recorded in", f)


def log_error(msg: str):
    error(msg)


def log_info(msg: str):
    info(msg)


# path.abspath(__file__) or figure out who's calling dglogger, think there is a feature for that
def log_start():
    info("Start")


def log_warning(msg: str):
    warning(msg)


print_err = partial(print, file=stderr)


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
    log_critical("Testing log_critical()")
    log_end()
