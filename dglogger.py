#! /usr/bin/env python3

# working from
# * http://inventwithpython.com/blog/2012/04/06/stop-using-print-for-debugging-a-5-minute-quickstart-guide-to-pythons-logging-module/
# * https://docs.python.org/3/howto/logging.html#a-simple-example

import logging
import os
import platform


def log_config():
    """Unique name by machine and user.
    OS X: ~/Library/Logs/<machine-name>_<username>.log

    :param home: $HOME directory for user running process
    :return: log file name
    """
    home = os.environ["HOME"]
    machine_user = str.split(platform.uname()[1], ".local")[0] \
        + "_" + os.getlogin()
    log_file_path = os.path.join(home, "Library/Logs/")
    if not os.path.isdir(log_file_path):
        log_file_path = home

    l_file = log_file_path + machine_user + ".log"

    logging.basicConfig(
      filename=l_file,
      format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
      datefmt='%m/%d/%Y %H:%M:%S',
      level=logging.INFO
    )
    return l_file


def log_end(f):
  logging.info(": End")
  print("Actions recorded in ", f, ".", sep = "")


def log_error(msg, indent = '\n    '):
  print(indent + msg, sep = "")
  logging.error(msg)


def log_info(msg, indent = '\n    '):
  print(indent + msg, sep = "")
  logging.info(msg)


def log_start():
  logging.info(": Start")


def log_warning(msg, indent = '\n    '):
  print(indent + msg, sep = "")
  logging.warning(msg)


#
# Test
#
def test():
    log_file = log_config()
    log_start()
    log_end(log_file)


# Revisit if this code will work on python (v2) as well
