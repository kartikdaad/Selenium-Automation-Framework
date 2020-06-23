import logging
import logging.config

class LoggingConfig():

    def testlog(self):

        # create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggingConfig.__name__)

        # logging messages
        logger.debug("debug message")
        logger.info("info message")
        logger.error("error message")
        logger.warning("warning message")
        logger.critical("critical message")

demo = LoggingConfig()
demo.testlog()