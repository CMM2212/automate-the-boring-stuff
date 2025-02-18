"""
Remove headers from a csv file
"""

import csv
import os


subdirectory = 'no_header'

def remove_header(file):
    """Remove header from csv file and resave it"""
    with open(file) as f:
        with open(os.path.join(subdirectory, file), 'w', newline='') as o:
            reader = csv.reader(f)
            writer = csv.writer(o)
            try:
                next(reader)
            except StopIteration:
                return
            writer.writerows(reader)
                

for file in os.listdir():
    if file.endswith('.csv'):
        remove_header(file)
        

        
        
with open('super_headers.csv') as f:
    reader = csv.reader(f)
    print(list(reader))
    for row in reader:
        print(row)
        
with open('fake.csv', 'w', newline='') as g:
    writer = csv.writer(g, delimiter='\t', lineterminator='\n-----------------\n')
    writer.writerow(['baby', 'cat', 'mama', 'rat'])
    writer.writerow(['super', 'dog', 'duper', 'hog'])
    writer.writerows((name for name in ['bobby', 'johnny', 'cowby', 'lalalana', 'ashby']) for i in range(10)) 