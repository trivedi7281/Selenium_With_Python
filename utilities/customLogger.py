import logging

class LogGen:
    @staticmethod
    def logger():
         logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)', datefmt='%m%d%Y %I:%M:%S %p')
         logger=logging.getLogger()
         logger.setLevel(logging.INFO)
         return logger