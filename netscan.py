#!/bin/python3

from scapy.all import *
import sys

if len(sys.argv) < 3:
    print("[-] Not enough Arguments")
    exit()

ip_range = sys.argv[1]
interface = sys.argv[2]
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range)

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
    print(receive.sprintf(r"%Ether.src% - %ARP.psrc%")) 