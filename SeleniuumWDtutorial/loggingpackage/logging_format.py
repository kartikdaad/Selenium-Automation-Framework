import logging

logging.basicConfig(filename="testing.log", format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %H:%M:%S %p", level=logging.DEBUG)  # (If H = 24hours format, I = 12 hours format)
logging.warning("Warning Message")
logging.info("info message")  # Won't be printed as it is above warning in level
logging.error("error message")
