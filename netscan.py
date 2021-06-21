import scapy.all as scapy
import argparse




subnet_range = "192.168.0.1/24"

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Adresses')
    options = parser.parse_args()

    if not options.target:
        parser.error("[netscan] error with ip")
    return options

def scan(ip):
    arp_req_frame = scapy.ARP(pdst = ip)

    broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")

    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
    answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout=1, verbose = False)[0]
    result = []
    for i in range(0, len(answered_list)):
        client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc}
        result.append(client_dict)
    f = open("dat.txt", "w")
    f.write(str(result))
    f.close()

scan("192.168.0.1/24")


# options = get_args()
# scanned_output = scan()
# send_email(scan(subnet_range))
