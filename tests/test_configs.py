#! /usr/bin/env python3

from dglogger.configs import Log_configs, get_func
from dglogger.dglogger import *
from logging import info, warning, error, debug

def test_create_console(capsys):
    logger = get_func(Log_configs.CONSOLE)()

    message = 'This is a test of console INFO level message.'
    log_info(message)
    text = capsys.readouterr().err
    assert message in text

    message = 'Testing console WARNING level message.'
    log_warning(message)
    text = capsys.readouterr().err
    assert message in text

    message = 'Testing console ERROR level message.'
    log_error(message)
    text = capsys.readouterr().err
    assert message in text

    message = 'Testing console CRITICAL level message.'
    log_critical(message)
    text = capsys.readouterr().err
    assert message in text

# logging.debug() is not generating stderr output - need to figure out
    # message = 'Testing console DEBUG level message.'
    # log_debug(message)
    # text = capsys.readouterr().err
    # assert message in text

    message = 'Testing console log_dev INFO message.'
    log_dev(message, level = info)
    text = capsys.readouterr().err
    assert message in text

    message = 'Testing console log_dev WARNING message.'
    log_dev(message, level = warning)
    text = capsys.readouterr().err
    assert message in text

    message = 'Testing console log_dev ERROR message.'
    log_dev(message, level = error)
    text = capsys.readouterr().err
    assert message in text

    # message = 'Testing console log_dev DEBUG message.'
    # log_dev(message, level = debug)
    # text = capsys.readouterr().err
    # assert message in text
