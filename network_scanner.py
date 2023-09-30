#!/usr/bin/env python

import scapy.all as scapy
import optparse


def scan(ip):
    # scapy.ls(class)  -> listera tutti gli attributi della classe
    # stiamo creando un pacchetto ARP con ip di destinazione quello che poi l'utente selezionera
    arp_request = scapy.ARP(pdst=ip)
    # stiamo creando un pacchetto con ethernet con mac di destinazione il broadcast mac
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # combiniamo i due pacchetti
    arp_request_broadcast = broadcast/arp_request
    # sending the packet -> non stiamo usando sr ma srp in quanto sta una custom ether part
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for answer in answered_list:
        client_dict = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def table_print(clients):
    print("IP\t\t\tMAC Address\n-------------------------------------------")
    for answer in clients:
        print(answer["ip"] + "\t\t" + answer["mac"] +
              "\n-------------------------------------------")


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip_address", help="ip or whole ip subnet (by adding /24 at the end")
    (options, arguments) = parser.parse_args()
    if not options.ip_address:
        parser.error("[-] Please enter a valid ip address or a valid ip subnet, use --help for more info")
    return options
