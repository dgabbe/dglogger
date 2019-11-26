from dglogger.configs import Log_configs, get_func

from dglogger.dglogger import *

def test_create_console(capsys):
    logger = get_func(Log_configs.CONSOLE)()
    message = 'This is a test of console INFO level message.'
    logger.setLevel(INFO)
    log_info(message)

    text = capsys.readouterr().err

    assert message in text

