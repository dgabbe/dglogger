# Capturing log messages: https://docs.pytest.org/en/5.1.2/logging.html
from logging import warning

from dglogger import (
    log_config,
    log_start,
    log_info,
    log_warning,
    log_error,
    log_debug,
    log_critical,
    log_dev,
    log_end,
)


# def test():
#     assert log_config() == None
#     assert log_start() == None
#     log_info("Testing log_info()")
#     log_warning("Testing log_warning()")
#     log_error("Testing log_error()")
#     log_debug("Testing log_debug()")
#     log_critical("Testing log_critical()")
#     log_dev("log_dev, info level")
#     log_dev("log_dev, warning level", warning)
#     log_dev("log_dev, foo, expecting exception", "foo")
#     log_devend()
