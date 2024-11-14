# A file to contain constant variables
# to make the program more efficient
from .encryption import load_key
from .utils import get_todays_date



ENCRYPTION_KEY =  load_key()
TODAYS_DATE = get_todays_date()
LOGGING_PATH = f'./Logs/{TODAYS_DATE}.log'