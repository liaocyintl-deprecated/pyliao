import os
import platform
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

if os.name == 'nt':
    DRIVER_PATH = 'drivers/chromedriver_win32.exe'
elif platform.system() == 'Darwin':
    DRIVER_PATH = 'drivers/chromedriver_mac64'
else:
    DRIVER_PATH = 'drivers/chromedriver_linux64'