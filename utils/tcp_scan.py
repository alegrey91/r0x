#!/usr/bin/env python3

import nmap as nm

NMAPSCAN = "-n -Pn -sS "

class TCPScan:

    def __init__(self, ipaddr, args):
        self.ipaddr = ipaddr
        self.args = NMAPSCAN + args


    """
    Print formatted output.
    """
    def print_output(self, nmap):
        for ip in nmap.all_hosts():
            ports = nmap[ip].all_tcp()
            print("[TCP]")
            print("PORT\tSTATUS\tPROTO\tVERSION")
            if len(ports) != 0:
                for port in ports:
                    info = dict(nmap[ip].tcp(port))
                    print("{}\t{}\t{}\t{} {} {}".format(port, 
                        info['state'], 
                        info['name'], 
                        info['product'],
                        info['version'], 
                        info['extrainfo']))
            else:
                print("-\t-\t-\t-")
            print()

    """
    Scan using a basic SYN scan.
    """
    def scan(self):
        # Scanning phase
        nmap = nm.PortScanner()
        nmap.scan(hosts=self.ipaddr, arguments=self.args)
        # Output formatting
        print("nmap {} {}".format(self.args, self.ipaddr))
        self.print_output(nmap)
        return nmap
