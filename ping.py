from scapy.all import *
import ipaddress

def SendPing(host):
    ans,unans = sr(
        IP(dst=host)/
        ICMP())
    print("results: %s:" % host)
    for (s, r) in ans:
        print("s: " % IP.version)
    

host = input("Enter IP to ping: ")

try:
    ipaddress.ip_address(host)
except:
    print("Invalid Address")
    exit(-1)

SendPing(host)