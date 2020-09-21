# snippet to implement log on scripts
# format: /path/log/SCRIPT-2019-01-23.log"

import logging
import time

log_time = time.strftime("%Y-%m-%d")
log_file = "/path/log/SCRIPT-" + log_time + ".log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger("SCRIPT")
logger.info('[{}] - [{}]: log message'.format(var01,var02))

# log line result
# 2019-01-23 12:34:20 - SCRIPT - INFO - [var01] - [var02]: log message
