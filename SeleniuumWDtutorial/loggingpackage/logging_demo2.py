import logging
import loggingpackage.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug("debug message")
        self.log.error("error message")
        self.log.info("info message")
        self.log.warning("warning message")
        self.log.critical("Critical message")

    def method2(self):
        m2log = cl.customLogger(logging.INFO)
        m2log.debug("debug message")
        m2log.error("error message")
        m2log.info("info message")
        m2log.warning("warning message")
        m2log.critical("Critical message")

    def method3(self):
        m3log = cl.customLogger(logging.INFO)
        m3log.debug("debug message")
        m3log.error("error message")
        m3log.info("info message")
        m3log.warning("warning message")
        m3log.critical("Critical message")

demo2 = LoggingDemo2()
demo2.method1()
demo2.method2()
demo2.method3()