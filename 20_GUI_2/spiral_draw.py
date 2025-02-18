#!/usr/bin/env python
"""Use in combination with a paint program to draw a spiral shape."""
import time

import pyautogui


def main():
    """Program begins here."""
    time.sleep(5)
    pyautogui.click()
    distance = 300
    change = 20
    while distance > 0:
        pyautogui.drag(distance, 0, duration=0.2)
        distance -= change
        pyautogui.drag(0, distance, duration=0.2)
        pyautogui.drag(-distance, 0, duration=0.2)
        distance -= change
        pyautogui.drag(0, -distance, duration=0.2)


if __name__ == '__main__':
    main()
