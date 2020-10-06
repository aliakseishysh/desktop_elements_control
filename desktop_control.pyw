from os import path
from os import environ
from os import listdir
from os import system
from os import getcwd
from os import curdir
from win10toast import ToastNotifier

PROFILE_PATH = environ['USERPROFILE']
PROFILE_NAME = PROFILE_PATH.split('\\')[-1]
DESKTOP_PATH = path.join(environ['USERPROFILE'], 'Desktop')
ELEMENTS = listdir(DESKTOP_PATH)
SCRIPT_DIR = '\\'.join(path.abspath(__file__).split('\\')[0:-1])
ICO_NAME = 'Python.ico'

if ELEMENTS.__len__() >= 13:
    toast = ToastNotifier()
    toast.show_toast('Desktop Control', 'Рабочий стол захламлён :c', duration=5, icon_path=path.join(SCRIPT_DIR, ICO_NAME))