# Capturing log messages: https://docs.pytest.org/en/5.1.2/logging.html

import dglogger

def test():
    assert log_config() == None
    assert log_start() == Name
    log_info("Testing log_info()")
    log_warning("Testing log_warning()")
    log_error("Testing log_error()")
    log_debug("Testing log_debug()")
    log_critical("Testing log_critical()")
    log_dev("log_dev, info level")
    log_dev("log_dev, warning level", warning)
    log_dev("log_dev, foo, expecting exception", 'foo')
    log_end()
