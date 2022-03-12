import logging


class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        f_handler = logging.FileHandler("/Users/mack/PycharmProjects/nopCommerceApp/Logs/automation.log")
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        f_handler.setFormatter(formatter)
        logger.addHandler(f_handler)
        logger.setLevel(logging.INFO)
        return logger
