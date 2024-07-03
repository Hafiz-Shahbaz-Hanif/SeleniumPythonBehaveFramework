import allure
from utilities.customLogger import LogGen


class MyException:
    logger = LogGen.loggen()

    def __init__(self):
        pass

    @staticmethod
    def handle_exception(context, exception):
        error_message = ' '.join(str(exception).split()[:40])
        MyException.logger.error(error_message)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        raise
