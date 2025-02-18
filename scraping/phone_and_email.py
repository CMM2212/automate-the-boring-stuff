import pyperclip
import re

phone_re = re.compile(r'''(
    (\d{3}|\(d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''',re.VERBOSE)

email_re = re.compile(r'''(
    [a-zA-z]+[a-zA-Z0-9\-\.\_]
    *@
    [a-zA-Z0-9]{2,}
    \.            
    [a-zA-Z]{2,}
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
    
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + group[8]
    matches.append(phone_num)
    
for groups in email_re.findall(text):
    matches.append(groups)
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('None found!')
    