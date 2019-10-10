#!/usr/bin/env python3

import nmap as nm

class TCPScan:

    def __init__(self, ip_addr, args):
        self.ip_addr = ip_addr
        self.args = args

    """
    Print formatted output.
    """
    def print_output(self, nmap):
        for ip in nmap.all_hosts():
            print("PORT\tSTATUS\tPROTO\tVERSION")
            for port in nmap[ip].all_tcp():
                info = dict(nmap[ip].tcp(port))
                print("{}\t{}\t{}\t{} {} {}".format(port, 
                    info['state'], 
                    info['name'], 
                    info['product'],
                    info['version'], 
                    info['extrainfo']))
            print()

    """
    Scan using a basic SYN scan.
    """
    def scan(self):
        # Scanning phase
        nmap = nm.PortScanner()
        nmap.scan(hosts=self.ip_addr, arguments=self.args)
        # Output formatting
        self.print_output(nmap)
        return nmap
