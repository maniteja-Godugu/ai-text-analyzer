import logging



def setup_logging():

    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler("logs/logs.log")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    