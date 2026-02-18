'''Configure Python's logging module with both a console handler (INFO level) and a file
handler (DEBUG level). Call a sample function that logs messages at all four levels.'''

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

format = logging.Formatter('%(asctime)s %(levelname)s %(message)s',
                           datefmt='%Y-%m-%d %H:%M')

#console Handler

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(format)

#file Handler

file = logging.FileHandler("app.log")
file.setLevel(logging.DEBUG)
file.setFormatter(format)

logger.addHandler(console)
logger.addHandler(file)

def sample_function():
    logger.debug("Debugging details")
    logger.info("App started")
    logger.warning("This is a warning")
    logger.error("Something failed")


if __name__ == "__main__":
    sample_function()