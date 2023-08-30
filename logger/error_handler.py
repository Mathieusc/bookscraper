import logging

def setup_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        filename="app.log",
                        filemode="a")
    
def log_error(error_message):
    logger = logging.getLogger(__name__)
    logging.error(error_message)

    
setup_logging()
