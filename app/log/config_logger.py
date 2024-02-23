import os
import logging.config

def setup_logging():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, 'logging_config.ini')
    logging.config.fileConfig(config_path, disable_existing_loggers=False)