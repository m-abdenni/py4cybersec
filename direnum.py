#!/bin/python3

import requests as req
import sys

if len(sys.argv) < 3:
	print('[-] Not enough arguments')
	exit()
wordlist = open(sys.argv[2]).read().split('\n')

for dir in wordlist:
	url = f'http://{sys.argv[1]}/{dir}.html'
	print(f'\r[*] Trying {dir}...',end='')
	r = req.get(url)

	if r.status_code != 404:
		s = r.status_code
		print()
		print(f'{s}    /{dir}')
		print()

