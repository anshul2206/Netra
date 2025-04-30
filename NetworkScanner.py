#!/usr/bin/env python

import scapy.all as scapy
import argparse


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for elements in answered_list:
        client_dic = {"ip": elements[1].psrc, "mac": elements[1].hwsrc}
        clients_list.append(client_dic)
    return clients_list


def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", dest="ipaddress", help="Provide an IP address")
    options = parser.parse_args()
    if not options.ipaddress:
        parser.error("[-] Please specify an IP address or range of IP address, use --help for more info")
    else:
        return options


def print_result(result_list):
    print("IP\t\t\t MAC Address\n-----------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_input()
scan_result = scan(options.ipaddress)
print_result(scan_result)
