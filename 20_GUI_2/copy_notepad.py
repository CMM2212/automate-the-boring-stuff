#!/usr/bin/env pytohn
"""Copy text from a notepad and print it out in Python."""
import pyautogui
import pyperclip


def main():
    """Switch to the open notepads window and print the text in it."""
    previous_window = pyautogui.getActiveWindow()
    window = pyautogui.getWindowsWithTitle('notepads')[0]
    window.activate()
    pyautogui.sleep(.05)
    pyautogui.keyDown('ctrl')
    pyautogui.write(['a', 'c'])
    pyautogui.keyUp('ctrl')
    text = pyperclip.paste()
    print(text)
    previous_window.activate()


if __name__ == '__main__':
    main()
