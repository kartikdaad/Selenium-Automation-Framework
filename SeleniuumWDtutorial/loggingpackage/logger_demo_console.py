"""
Logger demo
"""
import logging
class LoggerDemoConsole():
    def testlog(self):
        #create Logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        #create formatter
        formatter = logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %H:%M:%S %p")

        # add formatter to console handler  -> chandler
        chandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(chandler)

        # logging messages
        logger.debug("debug message")
        logger.info("info message")
        logger.error("error message")
        logger.warning("warning message")
        logger.critical("critical message")

demo = LoggerDemoConsole()
demo.testlog()