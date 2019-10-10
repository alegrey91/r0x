#!/usr/bin/env python3

from . import variables
import subprocess
import os
import re
import nmap as nm

UNICORNSCAN = "unicornscan -mU -r200 {}"
NMAPSCAN = "-sU --host-timeout 400 -sV -p{} "

"""
UDP Scan using unicornscan.
"""
class UDPScan:

    def __init__(self, ipaddr):
        self.ipaddr = ipaddr

    """
    Perform a preliminary fast scan using unicornscan,
    then pass the result to an exaustive nmap scan.
    """
    def fast_scan(self):
        # print("starting UDP scan")
        cmd = UNICORNSCAN.format(self.ipaddr)
        # print(cmd)
        res = subprocess.Popen(cmd.split(), \
                stdout=subprocess.PIPE, \
                universal_newlines = True)
        ports = []
        for line in res.stdout:
            res_regex = re.match(r"(\d+)", line.split()[3])
            if res_regex: 
                port = res_regex.group(1)
                ports.append(port)
        return ports

    """
    Print formatted output.
    """
    def print_output(self, nmap):
        for ip in nmap.all_hosts():
            print("[{}]".format(ip))
            print("PORT\tSTATUS\tPROTO\tVERSION")
            for port in nmap[ip].all_udp():
                info = dict(nmap[ip].udp(port))
                print("{}\t{}\t{}\t{} {} {}".format(port, 
                    info['state'], 
                    info['name'], 
                    info['product'],
                    info['version'], 
                    info['extrainfo']))
            print()

    """
    Using the output provided by unicorn scan,
    perform an exaustive scan using nmap.
    """
    def scan(self):
        ports = variables.top_udp_ports #self.fast_scan()
        udp_ports = ','.join(ports)
        arguments = NMAPSCAN.format(udp_ports)
        #print("nmap {} {}".format(arguments,self.ipaddr))
        nmap = nm.PortScanner()
        nmap.scan(hosts=self.ipaddr, arguments=arguments)
        # Output formatting
        self.print_output(nmap)
        return nmap
