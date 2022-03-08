import logging

class LogGen:
    @staticmethod
    def loggen():

    logging.basicConfig(filename=".\\Logs\\automation.log"

format= '%(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%m:%s %P')
    logger=logging.getlogger()
    logger.setlevel(logging.INFO)
    return logger