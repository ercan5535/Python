import logging
import logging.config
logging.config.fileConfig('logging/logging.conf')

logger=logging.getLogger(__name__)
logger.debug('this is a debug message')