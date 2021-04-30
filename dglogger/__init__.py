name = "dglogger"  # For PyPi, still used?
__name__ = "dglogger"
__package__ = "dglogger"

from .configs import Log_configs

from .dglogger import (
    log_critical,
    log_debug,
    log_dev,
    log_end,
    log_error,
    log_info,
    log_start,
    log_warning,
)
