from enum import Enum, auto
import dglogger

class Log_configs(Enum):
    CONSOLE = auto()
    LOG_FILE = auto()
    LOG_FILE_AND_CONSOLE = auto()
    LOG_FILE_REQUIRED = auto()

def get_func(which: Log_configs):
    f_dict = {
        Log_configs.CONSOLE: dglogger.dglogger.instantiate_console,
        Log_configs.LOG_FILE: {},
        Log_configs.LOG_FILE_AND_CONSOLE: {},
        Log_configs.LOG_FILE_REQUIRED: {},
    }
    return f_dict[which]
