#!/usr/bin/env python

import network_scanner as scanner

options = scanner.get_arguments()
ip = options.ip_address
scan_answers = scanner.scan(ip)
# scan_answers = scan("192.168.86.1/24")
scanner.table_print(scan_answers)
