# -----------------------------------------------------------
# Demonstrates how to draw a circle using
# pyautogui,pywinauto in microsoft windows mspaint application
#
# Email saxena.k989@gmail.com
# -----------------------------------------------------------

import math
import sys
import time

import psutil
import pyautogui
from pywinauto.application import Application

windowsapp = 'mspaint.exe'
pyautogui_wait_time = 5
task_wait = 2


class Circle:

    # launch windows application (mspaint)
    def launchWindowsApp(self):
        # sleep 10 seconds for pyautogui setup
        time.sleep(pyautogui_wait_time)
        # Run windows paint  application
        self.app = Application().start(windowsapp).top_window()
        # click to transfer focus on mspaint application
        pyautogui.click()

    def drawCircle(self, R):
        # get display resolution coordinates
        (x, y) = pyautogui.size()
        # center coordinates of the display
        (X, Y) = pyautogui.position(x / 2, y / 2)
        # offsetting by radius
        pyautogui.moveTo(X + R, Y)

        for i in range(360):
            # set the arc precision for circle
            if i % 2 == 0:
                # Mouse down to start drawing
                pyautogui.mouseDown(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))
                # Moving pointer to draw a circle
                pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))

    # terminate mspaint application process
    def terminateApp(self):
        # wait for 2 seconds - let the drawing process gets completed
        time.sleep(task_wait)
        for proc in psutil.process_iter():
            if proc.name() == windowsapp:
                proc.kill()
                print("Application terminated successfully.")
                sys.exit(1)


if __name__ == '__main__':
    instance = Circle()
    # Radius of a circle
    R = 300
    instance.launchWindowsApp()
    instance.drawCircle(R)
    instance.terminateApp()
