import logging
import os
from datetime import datetime
import os

#This is the log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M_%S')}.log"

#This is the logging directory
LOG_FILE_DIR = os.path.join(os.getcwd(), "logs")

#Create folder if not available
os.makedirs(LOG_FILE_DIR, exist_ok = True)

#Log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename =LOG_FILE_NAME,
    format ="[%(asctime)s ] %(lineo)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)