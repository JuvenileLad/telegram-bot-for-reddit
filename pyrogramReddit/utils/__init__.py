import logging
from configparser import ConfigParser
from datetime import datetime
from io import BytesIO, StringIO
from .db_handler import subDB, user_in_DB, sub_in_DB, list_db
from .reddit_handler import Check_sub, get_data

# Logging at the start to catch everything
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING,
    handlers=[
        logging.StreamHandler()
    ]
)
LOGS = logging.getLogger(__name__)