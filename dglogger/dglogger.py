#! /usr/bin/env python3

# working from
# * http://inventwithpython.com/blog/2012/04/06/stop-using-print-for-debugging-a-5-minute-quickstart-guide-to-pythons-logging-module/
# * https://docs.python.org/3/howto/logging.html#a-simple-example
# * Eric's code ideas: https://gist.github.com/eric-s-s/11e08dbc38891fa3d0eba5396703afc6
# * Eric's setup.py: <<get github link>>
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
from platform import uname
from pwd import getpwnam
from sys import exit, stderr
import dglogger.configs

# Conditional formatting possible based on levelname?
def get_stream_handler() -> StreamHandler:
    # By default goes to stderr
    stream_formatter = Formatter(
        fmt="    [%(asctime)s] %(levelname)s %(module)s:%(lineno)d %(message)s",
        datefmt="%H:%M:%S",
    )
    handler = StreamHandler()
    handler.setFormatter(stream_formatter)
    return handler


def log_config_new(
    config="console", config_dict=dglogger.configs, is_log_file_required: bool = False
) -> Logger:
    pass


def instantiate_console():
    logger = getLogger()
    console_handler = get_stream_handler()
    logger.addHandler(console_handler)
    return logger


def instantiate_tqdm_progress():
    pass


# Can this be called from __init__.py so it's running before main()?
def log_config(is_log_file_required: bool = False) -> Logger:
    """Unique name by machine and user.
    OS X: ~/Library/Logs/<machine-name>_<username>.log

    References:
    - https://docs.python.org/3/library/logging.html
    - https://docs.python.org/3/howto/logging-cookbook.html#logging-to-multiple-destinations

    :return: Logger object
    """
    log_file_name = create_log_file_name()
    try:
        basicConfig(
            filename=log_file_name,
            format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
            level=INFO,
        )
    except (PermissionError, FileNotFoundError):
        exception(f"Could not create log file at: {log_file_name}")
        if is_log_file_required:
            exit("No log file requires this program to stop.")

    logger = getLogger()
    console_handler = get_stream_handler()
    logger.addHandler(console_handler)
    return logger


def create_log_file_name():
    user = getlogin()
    home_dir = getpwnam(user).pw_dir
    machine_user = str.split(uname()[1], ".local")[0] + "_" + user
    log_file_path = path.join(home_dir, "Library/Logs/")  # MacOS location
    if not path.exists(log_file_path):
        log_file_path = home_dir  # Linux location
    log_file_name = path.join(log_file_path, machine_user + ".log")
    return log_file_name


def log_critical(msg: str):
    critical(msg)


def log_debug(msg: str):
    debug(msg)


def log_end():
    # https://stackoverflow.com/questions/26017073/how-to-get-filename-from-a-python-logger
    f = getLogger().handlers[0].baseFilename
    info("End")
    shutdown()
    print("Actions recorded in", f)


def log_error(msg: str):
    error(msg)


def log_info(msg: str):
    info(msg)


# path.abspath(__file__) or figure out who's calling dglogger, think there is a feature for that
def log_start():
    info("Start")


def log_warning(msg: str):
    warning(msg)


def log_dev(msg: str, dev: str = "unknown", level=info):
    try:
        level("[" + dev + "] " + msg)
    except:
        print(">>>Oops - Complete log_dev() implementation!", file=stderr)
