import sys
import hashlib
import pyfiglet

banner = pyfiglet.figlet_format("Python Hash Cracker")
print(banner)

if len(sys.argv) < 4:
    print('[!] Usage:')
    print('python hashcracker.py [hash] [format] [wordlist]')
    exit()

cipher = sys.argv[1]
form = sys.argv[2]
wordlist = sys.argv[3]

if hasattr(hashlib, form):
    hash_func = getattr(hashlib, form)
else:
    print('Invalid format')
    exit()

with open(wordlist, 'r') as file:
    for line in file.readlines():   
        print(f"\r[*] Trying {line}...", end="")
        hash_ob = hash_func(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == cipher:
            print()
            print()
            print('[+] Found cleartext password!: ' + line.strip())
            exit(0)