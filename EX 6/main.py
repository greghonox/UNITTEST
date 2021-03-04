import os
import requests

def url_exists(url):
    r = requests.get(url)
    if r.status_code == 200:
        return True

    elif r.status_code == 404:
        return False

def process_response(url):
    r = requests.get(url)
    return r.content

def download(url):
    r = requests.get(url)
    filename = os.path.basename(url)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(r.text)

if(__name__ == '__main__'):
    url_c = 'http://google.com/nonexistingurl'
    url_e = 'https://google.com.br'
    print(url_exists(url_e))
    print(url_exists(url_c))
    print(process_response(url_c))
    print(download(url_c))