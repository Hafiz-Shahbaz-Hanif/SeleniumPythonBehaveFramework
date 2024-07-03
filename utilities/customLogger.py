import logging
import time


class LogGen:

    logger_initialized = False

    @staticmethod
    def loggen():
        if not LogGen.logger_initialized:
            logger = logging.getLogger()
            logger.propagate = False
            curr_datetime = time.strftime("%Y-%m-%d _ %H-%M-%S")
            fhandler = logging.FileHandler(filename='.\\Logs\\log_ ' + curr_datetime + '.log')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.INFO)
            LogGen.logger_initialized = True
        else:
            logger = logging.getLogger()

        return logger