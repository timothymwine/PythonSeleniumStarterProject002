import os
import logging

class LogGen:
    """
    - This is method is used for logging info and it will create a logs folder incase it doesn't exist
    - This method 
    """
    @staticmethod
    def loggen():
        log_directory = ".//logs/"
        os.makedirs(log_directory, exist_ok=True)  # Create the directory if it doesn't exist

        log_file_path = os.path.abspath(os.path.join(log_directory, "automation.log"))
        # log_file_path = os.path.abspath(".//logs/automation.log")
        logging.basicConfig(filename=log_file_path, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger