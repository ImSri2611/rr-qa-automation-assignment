import logging

def get_logger():
    logger = logging.getLogger()
    if not logger.handlers:
        file_handler = logging.FileHandler("logs/test.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
    return logger
