#! /usr/bin/env python3

# working from
# * http://inventwithpython.com/blog/2012/04/06/stop-using-print-for-debugging-a-5-minute-quickstart-guide-to-pythons-logging-module/
# * https://docs.python.org/3/howto/logging.html#a-simple-example
# * Eric's code ideas: https://gist.github.com/eric-s-s/11e08dbc38891fa3d0eba5396703afc6
# * Eric's setup.py: <<get github link>>

# Packaging links:
# * https://stackoverflow.com/questions/47193079/module-vs-package
# * https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package

# Questions to research
# instantiate_log_file(): Can this be called from __init__.py so it's running before main()?
from logging import (
    basicConfig,
    critical,
    debug,
    DEBUG,
    error,
    ERROR,
    exception,
    FileHandler,
    Formatter,
    getLogger,
    INFO,
    info,
    Logger,
    shutdown,
    StreamHandler,
    warning,
    WARNING,
)
from os import getuid, path
from platform import uname
from pwd import getpwnam, getpwuid
from sys import exit, stderr
#import .configs

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


# part of instantiate_log_file
def get_file_handler() -> FileHandler:
    log_file_name = create_log_file_name()

    # log_directory = os.path.join(home_path, mac_os_log_directory)
    # if not os.path.exists(log_directory):
    #     log_directory = os.path.join(home_path, 'Logs')
    #     if not os.path.exists(log_directory):
    #         os.mkdir(log_directory)
    # full_log_file_path = os.path.join(log_directory, log_file_name)
    fh = FileHandler(log_file_name)
    # start coding here!!!
    file_formatter = Formatter(
        fmt="{asctime} {filename} {levelname}: {message}",
        datefmt="%m/%d/%Y %H:%M:%S",
        style="{",
    )
    fh.setFormatter(file_formatter)
    return fh


def instantiate_console() -> Logger:
    logger = getLogger()
    console_handler = get_stream_handler()
    logger.addHandler(console_handler)
    logger.setLevel(INFO)
    return logger


def instantiate_dev_console():
    pass


# Wonder if this should be a file handler so you can 'tail' it.
def instantiate_tqdm_progress() -> Logger:
    logger = getLogger()
    progress_handler = get_stream_handler()
    logger.addHandler(progress_handler)
    logger.setLevel(INFO)
    return logger


# start here!!! add option file name parameter
def instantiate_log_file(file_name, is_log_file_required: bool = False) -> Logger:
    """Defaults to
    OS X: ~/Library/Logs/<machine-name>_<username>.log
    Linux: ~/<machine-name>_<username>.log

    Optional file_name argument.

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

    return  # figure out if it makes sense to return a handler


def create_log_file_name() -> str:
    #
    # MacOS specific: Launched PyCharm-CE using Spotlight (⌘ space). In the Python Console,
    # getlogin() returned '_spotlight'. Use getpwuid() instead.
    user = getpwuid(getuid())[0]
    machine = str.split(uname()[1], ".local")[0]
    log_file_name = machine + "_" + user
    home_dir = getpwnam(user).pw_dir
    log_file_dir = path.join(home_dir, "Library/Logs/")  # MacOS location
    if not path.exists(log_file_dir):
        log_file_dir = home_dir  # Linux location
    log_file_path = path.join(log_file_dir, log_file_name + ".log")
    return log_file_path


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
