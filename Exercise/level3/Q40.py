'''Set up a logger using RotatingFileHandler so log files rotate after 2 KB and keep 3 backups.
Simulate 300 log entries and verify the backup files are created.'''

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler(
    'app.log',
    maxBytes=2048,
    backupCount=3
)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

for i in range(1,301):
    logger.info(f"This is log message number {i}")

print("Logging complete. Check app.log and rotated files!")
