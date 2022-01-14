import logging


class LoginGeneration:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='.\\logs\\auto.log',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
