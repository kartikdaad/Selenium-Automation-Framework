"""
Logging Demo1
Logging Level
Debug
Info
Warning
Error
Critical
"""
import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG)
logging.warning("Warning Message")
logging.info("info message")  # Won't be printed as it is above warning in level
logging.error("error message")


