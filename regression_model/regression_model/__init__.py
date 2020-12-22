import logging
from pathlib import Path 
from regression_model.config import config 
from regression_model.config import logging_config

PACKAGE_ROOT = Path(__file__).resolve().parent
VERSION_PATH = PACKAGE_ROOT / 'VERSION'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False

with open(VERSION_PATH, 'r') as version_file:
    __version__ = version_file.read().strip()