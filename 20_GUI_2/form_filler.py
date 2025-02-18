#!/usr/bin/env python
"""
Automate the process of submitting forms on autbor.com/form by retrieving
the data from a csv file and using GUI automation to enter in the information
"""
import csv
import webbrowser

import pyautogui


FILENAME = 'data.csv'
URL = 'https://autbor.com/form'
INTERVAL = 0.5
LOAD_WAIT = 3
POWERS = ['Wand', 'Amulet', 'Discount crystal ball', 'Money (e.g. Batman)']


def main():
    """Programs begins here."""
    data = get_csv_data()
    webbrowser.open(URL)
    for name, fear, power, robocop_rating, comments in data:
        submit_form(name, fear, power, robocop_rating, comments)
        new_form()
    print(f'Finished submitting {len(data)} forms')


def get_csv_data(filename):
    """Open and process the data in the given csv file and return a list of
    lists representing the data for each individual."""
    data = []
    with open(filename) as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            if not line:
                continue
            name, fear, power, robocop_rating, comments = line
            
            if fear == '':
                fear = None
                
            if robocop_rating == '':
                robocop_rating = None
            else:
                robocop_rating = int(robocop_rating) - 1
                
            if comments == '':
                comments = None
                
            power = POWERS.index(power) + 1
            data.append([name, fear, power, robocop_rating, comments])
    return data
                

def submit_form(name, fear, power, robocop_rating, comments):
    """Enter in the given information into the form and submit."""
    pyautogui.sleep(LOAD_WAIT)
    pyautogui.write(['tab'] * 4, INTERVAL)
    pyautogui.write(name)
    pyautogui.write(['tab'], INTERVAL)
    if fear:
        pyautogui.write(fear)
    pyautogui.write(['tab'] + ['down'] * power + ['enter', 'tab'], INTERVAL)
    if robocop_rating:
        pyautogui.write(['space'] + ['right'] * robocop_rating + ['tab'], INTERVAL)
    pyautogui.write(['tab'], INTERVAL)
    if comments:
        pyautogui.write(comments)
    pyautogui.write(['tab'], INTERVAL)
    pyautogui.write(['enter'], INTERVAL)
    print(f'Submitted form for {name}')
    

def new_form():
    """Click the link to start a new form."""
    pyautogui.sleep(LOAD_WAIT)
    pyautogui.write(['tab', 'enter'], INTERVAL)
    
    
    
if __name__ == '__main__':
    main()
