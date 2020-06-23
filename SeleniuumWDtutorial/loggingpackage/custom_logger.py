import logging
import  inspect
def customLogger(logLevel):
    # get the name of the class / method from where this method is called
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)

    # by default , log all message
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("{0}.log", format(loggername), mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %H:%M:%S %p")

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger