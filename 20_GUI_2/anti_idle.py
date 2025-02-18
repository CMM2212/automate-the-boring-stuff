#!/usr/bin/env pytohn
"""Slightly move the mouse every 10 minutes to prevent being idle."""
import pyautogui

TEN_MINUTES = 600

def main():
    """
    Repeatedly sleep for 10 minutes then move the mouse up and down 1 pixel
    """
    while True:
        pyautogui.sleep(TEN_MINUTES)
        pyautogui.move(1,0)
        pyautogui.move(-1,0)
    

if __name__ == '__main__':
    main()
    