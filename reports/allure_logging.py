import logging
import allure


class AllureHandler(logging.Handler):
    def emit(self, record):
        allure.attach(record.getMessage(), name=record.levelname, attachment_type=allure.attachment_type.TEXT)


# Configure root logger
allure_handler = AllureHandler()
logger = logging.getLogger()
logger.addHandler(allure_handler)
logger.setLevel(logging.INFO)
