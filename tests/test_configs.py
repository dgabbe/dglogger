#! /usr/bin/env python3

from dglogger.configs import Log_configs, get_func
from logging import INFO, WARNING, ERROR, DEBUG

from dglogger.dglogger import *

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

    message = 'Testing console DEBUG level message.'
    log_debug(message)
    text = capsys.readouterr().err
    assert message in text

    message = 'Testing console log_dev INFO message.'
    log_dev(message, level = INFO)
    text = capsys.readouterr().err
    assert message in text

    message = 'Testing console log_dev WARNING message.'
    log_dev(message, level = WARNING)
    text = capsys.readouterr().err
    assert message in text

    message = 'Testing console log_dev ERROR message.'
    log_dev(message, level = ERROR)
    text = capsys.readouterr().err
    assert message in text

    message = 'Testing console log_dev DEBUG message.'
    log_dev(message, level = DEBUG)
    text = capsys.readouterr().err
    assert message in text
