#!/usr/bin/env python
"""Clicks the colab logo if it is on the screen."""
import pyautogui
import cv2


def main():
    """Program begins here."""
    location = pyautogui.locateOnScreen('colab.png', confidence=.9)
    if location is not None:
        print("Clicking image")
        center = pyautogui.center(location)
        pyautogui.click(center.x, center.y, interval=0.1)
    else:
        print("Could not find image")
    

if __name__ == '__main__':
    main()
