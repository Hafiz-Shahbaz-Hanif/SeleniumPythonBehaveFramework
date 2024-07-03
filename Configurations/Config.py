from selenium import webdriver
import logging


class Config:
    def __init__(self, driver):
        self.driver = driver
        self.logger = self.setup_logger()

    def setup_logger(self):
        # Configure logging settings
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)
        return logger

    def launch_browser(self):
        self.driver = webdriver.Chrome()
        self.logger.info("**********  Browser Launched Successfully  **********")


# Create an instance of the Config class
config = Config()
