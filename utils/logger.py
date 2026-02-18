"""
Create a shared logger with a clean timestamp format
One instance imported so the app doesn't crash if a var is missing
"""


import logging
import sys
def get_logger(name: str = "medical_chatbot") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:  # Avoid adding duplicate handlers on re-import
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)  # Print logs to terminal
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
logger = get_logger()  # Shared logger instance — import this in other modules