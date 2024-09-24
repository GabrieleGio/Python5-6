from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.http import HTTPRequest 
from scapy.layers.http import HTTPResponse

iPkt = 0

def process_pkt(pkt):
    global iPkt 
    iPkt += 1
    print(f"ho ricevuto un pacchetto {iPkt} lungo {pkt[IP].len}, indirizzo IP di invio: {pkt[IP].src}, indirizzo ip di destinazione: {pkt[IP].dst}")

sniff(iface="eth0", filter="tcp", prn=process_pkt)