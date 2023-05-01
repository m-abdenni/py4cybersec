#!/bin/python3

import requests as req
import sys

if len(sys.argv) != 3:
	print("[-] Not enough arguments")
	print("[!] Please supply a domain name, and a subdomain wordlist")
	exit(1)

wordlist = open(sys.argv[2]).read().split('\n')

for sub in wordlist:
	url = f'http://{sub}.{sys.argv[1]}/'

	try:
		req.get(url)
	except req.ConnectionError:
		pass
	else:
		print('[+] Valid domain: ', url)


