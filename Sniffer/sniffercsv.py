from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.http import HTTPRequest, HTTPResponse
import csv
import time

iPkt = 0

csv_file = 'packets.csv'

# Funzione per scrivere i dati nel file CSV
def write_csv_row(packet_number, timestamp, host, src_ip, dst_ip, src_port, dst_port):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            packet_number,
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp)),
            host,
            src_ip,
            dst_ip,
            src_port,
            dst_port
        ])

# Crea un writer CSV e scrivi l'intestazione
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Packet Number', 'Timestamp', 'Host', 'Source IP', 'Destination IP', 'Source Port', 'Destination Port'])

def process_pkt(pkt):
    global iPkt
    iPkt += 1
    
    if IP in pkt and TCP in pkt:
        ip_layer = pkt[IP]
        tcp_layer = pkt[TCP]

        # Ottieni data e ora del pacchetto
        timestamp = pkt.time  # Tempo di ricezione del pacchetto

        # Ottieni porte TCP
        src_port = tcp_layer.sport
        dst_port = tcp_layer.dport

        if pkt.haslayer(HTTPRequest):
            # Ottieni l'host dalla richiesta HTTP
            if dst_port == 80:
                host = pkt[HTTPRequest].Host.decode() if pkt[HTTPRequest].Host else ""

        elif pkt.haslayer(HTTPResponse):
            # Ottieni l'host dalla risposta HTTP
            if src_port == 80:
                host = pkt[HTTPResponse].Server.decode() if pkt[HTTPResponse].Server else ""

        # Scrivi i dati nel file CSV
        if dst_port==443 or src_port == 443:
            host = "Host Criptato"
            write_csv_row(iPkt, timestamp, host, ip_layer.src, ip_layer.dst, src_port, dst_port)

# Inizia il sniffing
sniff(iface="eth0", filter="tcp", prn=process_pkt)