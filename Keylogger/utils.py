from datetime import datetime as dt
from win32gui import GetWindowText, GetForegroundWindow

def get_time() -> str:
    '''
    Return time in the following format

    [hh:mm:ss]
    '''
    return f'[{dt.now().hour}:{dt.now().minute}:{dt.now().second}]'


def get_active_window() -> str:
    return GetWindowText(GetForegroundWindow())


def get_todays_date() -> str:
    '''
    Return today's date in DD-MM-YYYY format
    '''
    now = dt.now()
    return f'{now.day}-{now.month}-{now.year}'
