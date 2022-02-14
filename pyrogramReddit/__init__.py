import logging
from configparser import ConfigParser
from datetime import datetime
from io import BytesIO, StringIO
from .client import *
from .main import *

# Logging at the start to catch everything
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING,
    handlers=[
        logging.StreamHandler()
    ]
)
LOGS = logging.getLogger(__name__)