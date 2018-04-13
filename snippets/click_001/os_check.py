import os
import platform
from enum import Enum

class OS_Type(Enum):
    WINDOWS      = 100
    LINUX        = 200
    MAC          = 300
    UNKNOWN      = 400

def check_os_type():
    osType = OS_Type.UNKNOWN
    os_name = platform.system()

    if os_name:
        name = os_name.lower()
        if 'linux' in name:
            osType = OS_Type.LINUX
        elif 'windows' in name:
            osType = OS_Type.WINDOWS
        elif 'darwin' in name:
            osType = OS_Type.MAC
    return osType

OS_TYPE = check_os_type()

