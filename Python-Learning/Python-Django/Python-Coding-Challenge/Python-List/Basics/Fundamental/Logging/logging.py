""" 
    Step 1: Understand the Basics (5 mins)
    Quickly go through this logging template and run it in your terminal or IDE:
"""
import logging

# Setup logging to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("This is a DEBUG message.")
logging.info("This is an INFO message.")
logging.warning("This is a WARNING message.")
logging.error("This is an ERROR message.")
logging.critical("This is a CRITICAL message.")


# 👉 You'll notice that only INFO and above is shown because of the level setting.

"""
    Try Log Rotation (Optional Advanced Task)
    Install Python’s logging.handlers for rotating logs:
"""

from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('library_rotating.log', maxBytes=1000, backupCount=3)
logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# This keeps logs from growing too big by rotating them once they hit 1KB (maxBytes=1000) and keeps 3 backups


