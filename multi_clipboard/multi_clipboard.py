import pyperclip
import sys
import json


json_file = 'multi_clipboard.json'

def loop():
    while True:
        command = input('>>>').split()
        with open(json_file, 'r') as file:
            keys = json.load(file)
            if command[0] == 'c' or command[0] == 'copy':
                if command[1]:
                    print(f'Saving clipboard to key {command[1]!r}')
                    keys[command[1]] = pyperclip.paste()
                else:
                    print('Error: Please provide a key to copy to')
                
            elif command[0] == 'v' or command[0] == 'paste':
                if command[1]:
                    if command[1] in keys:
                        print(f'Key {command[1]!r} copied to clipboard')
                        pyperclip.copy(keys[command[1]])
                    else:
                        print(f'Key {command[1]!r} not found')
                else:
                    print('Error: Please provide a key to copy from')
                
            elif command[0] == 'l' or command[0] == 'list':
                print('List of current keys:')
                for key in keys:
                    print(f'\t{key!r}')
                
            elif command[0] == 'd' or command[0] == 'delete':
                if command[1]:
                    print(f'Deleting key {command[1]!r}')
                    if command[1] in keys:
                        print(f'Key {command[1]!r} deleted')
                        keys.pop(command[1])
                    else:
                        print(f'Key {command[1]!r} not found')
                else:
                    print('Error: Please provide a key to delete')
            
            elif command[0] == 'h' or command[0] == 'help':
                print('Commands:')
                print("'c <key>': copies from clipboard and saves as specified key")
                print("'v <key>': copies to clipboard from specified key")
                print("'d <key>': deletes stored key")
                print("'l': lists all currently saved keys")
                print("'h': lists all commands")
                print("'q': quits program")
                
            elif command[0] == 'q' or command[0] == 'quit':
                print('Exiting')
                quit()
        with open(json_file, 'w') as file:
            json.dump(keys, file)

loop()
    