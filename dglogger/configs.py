from enum import Enum, auto
# import dglogger

class Log_configs(Enum):
    NOT_IMPLEMENTED = auto()
    CONSOLE = auto()
    DEV_CONSOLE = auto()
    LOG_FILE = auto()
    LOG_FILE_AND_CONSOLE = auto()
    LOG_FILE_REQUIRED = auto()
    TQDM_PROGRESS = auto()

# BUG - No exception handling for Log_configs that don't have a function
# Catch as NotImplementedError
def get_func(which: Log_configs):
    f_dict = {
        Log_configs.CONSOLE: dglogger.dglogger.instantiate_console,
        Log_configs.DEV_CONSOLE: dglogger.dglogger.instantiate_dev_console(),
        Log_configs.LOG_FILE: dglogger.dglogger.instantiate_log_file(),
        Log_configs.LOG_FILE_REQUIRED: dglogger.dglogger.instantiate_log_file(is_log_file_required = True),
    }
    return f_dict[which]
