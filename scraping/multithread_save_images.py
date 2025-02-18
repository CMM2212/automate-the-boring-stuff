import requests
import os
from bs4 import BeautifulSoup as bs
import threading
from math import ceil

os.makedirs('xkcd_comics', exist_ok=True)

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        print(f'Downloading page http://xkcd.com/{url_number}')
        response = requests.get(f'https://xkcd.com/{url_number}')
        response.raise_for_status()
        
        soup = bs(response.text, 'html.parser')
        
        comic_element = soup.select('#comic img')
        if comic_element == []:
            print(f'Could not find comic image on page {url_number}')
        else:
            comic_url = comic_element[0].get('src')
            print(f'Downloading image {comic_url}...')
            response = requests.get(f'https:{comic_url}')
            response.raise_for_status()
            
            with open(os.path.join('xkcd_comics', os.path.basename(comic_url)),
                      'wb') as image_file:
                for chunk in response.iter_content(10000):
                    image_file.write(chunk)
                    
def multithread_dowload(start, end, batch_size):
    end_comic = ceil((end - start) // batch_size)
    all_threads = []
    for i in range(start, end, end_comic):
        print('Creating thread')
        download_thread = threading.Thread(target=download_xkcd,
                                           args=[i, i + end_comic])
        download_thread.start()
        all_threads.append(download_thread)
        
    for thread in all_threads:
        download_thread.join()
        
    print('Finished.')
    
        
multithread_dowload(1,100,25)
