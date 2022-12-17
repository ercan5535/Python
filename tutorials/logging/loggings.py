import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
# default only these three are logged
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt='%m/%d/%Y %H:%M:%S', force=True)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
# 10/30/2022 13:02:30 - root - DEBUG - This is a debug message
# 10/30/2022 13:02:30 - root - INFO - This is an info message
# 10/30/2022 13:02:30 - root - WARNING - This is a warning message
# 10/30/2022 13:02:30 - root - ERROR - This is an error message
# 10/30/2022 13:02:30 - root - CRITICAL - This is a critical message

import logging.logging_helper as logging_helper
# 10/30/2022 13:13:04 - logging_helper - INFO - hello from helper

