import logging
from datetime import datetime
import os

#create log folder
LOG_DIR="housing_logs"

#we need current time for logging
CURRENT_TIME_STAMP= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"

#to create log directory and if already exist then no need to create new

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(name)s-%(levelname)s-%(message)s',
level=logging.INFO

)