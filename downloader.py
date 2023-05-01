
import sys
import requests as req
import pyfiglet

banner = pyfiglet.figlet_format("Python File Downloader")
print(banner)

if len(sys.argv) < 2:
    print('[-] Not enough arguments')
    print('[-] The file url is missing')
    exit()

url = sys.argv[1]
name = ''
try:
	name = sys.argv[2]
except:
	name = url.split('/')[-1]

res = req.get(url, allow_redirects=True)

print('[*] Downloading ...')

open(name, 'wb').write(res.content)

print(f'[+] File saved as {name}')
