import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("test.log")
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler.setFormatter(format)

logger.addHandler(handler)


logger.info("Information regarding testing logs")
logger.warning("Warning for testing logs")