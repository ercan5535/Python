import logging
import time
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 'kB, and keep backup logs app.log.1, app.log.2, etc
#handler = RotatingFileHandler('logging/app.log', maxBytes=2000, backupCount=5)
#logger.addHandler(handler2)

#for _ in range(1000):
#    logger.info("Hello world")

# s, m, h, d, midnight, w

handler2 = TimedRotatingFileHandler('logging/timed_test.log', when='s', interval=5, backupCount=5)
# every 5 seconds
logger.addHandler(handler2)

for _ in range(10):
    logger.info("Hello world")
    time.sleep(4)


