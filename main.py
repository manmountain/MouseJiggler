import pyautogui as pag
import win32api
import random
import time
import sys
import signal
from infi.systray import SysTrayIcon
import pygetwindow as gw


running = True;

if sys.platform == 'win32':
    from ctypes import *


    class LASTINPUTINFO(Structure):
        _fields_ = [
            ('cbSize', c_uint),
            ('dwTime', c_int),
        ]


    def get_idle_duration():
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
            millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
            return millis / 1000.0
        else:
            return 0
else:
    def get_idle_duration():
        return 0


def MoveMouse():
    win = gw.getWindowsWithTitle('Microsoft Teams')[0]
    win.restore()
    win.activate()
    br = win.bottomright
    bl = win.bottomleft
    tl = win.topleft
    while running:
        x = random.randint(bl[0], br[0])
        y = random.randint(tl[1], bl[1])
        pag.moveTo(x, y, 0.5)
        savedpos = win32api.GetCursorPos()
        time.sleep(1)
        curpos = win32api.GetCursorPos()
        if savedpos != curpos:
            break


def on_quit_callback(systray):
    global running
    running = False


def sigint_handler(signum, frame):
    global running
    running = False


signal.signal(signal.SIGINT, sigint_handler)


if __name__ == '__main__':
    systray = SysTrayIcon("bell-sleep-outline.ico", "Mouse Jiggler", None, on_quit=on_quit_callback)
    systray.start()
    while running:
        idle = get_idle_duration()
        if idle > 240:  # 4min
            systray.update(icon="bell-sleep.ico")
            MoveMouse()
            systray.update(icon="bell-sleep-outline.ico")

        time.sleep(1)

    systray.shutdown()
