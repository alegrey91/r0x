"""
Author: Alessio Greggi
Description:
Class to automate udp scanning process.
"""
import subprocess
import os
import re
import nmap as nm

UNICORNSCAN = "unicornscan -mU -r200 {}"
NMAPSCAN = "-sU --host-timeout 400 -sV "
top_ports = "--top-ports 50 "


"""
UDP Scan using unicornscan.
"""
class UDPScan:


    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.args = NMAPSCAN + top_ports
        self.nmap = nm.PortScanner()


    """
    Perform a preliminary fast scan using unicornscan,
    then pass the result to an exaustive nmap scan.
    """
    def fast_scan(self):
        cmd = UNICORNSCAN.format(self.ipaddr)
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
    def print_output(self):
        for ip in self.nmap.all_hosts():
            ports = self.nmap[ip].all_udp()
            print("[UDP]")
            print("PORT\tSTATUS\tPROTO\tVERSION")
            if len(ports) != 0:
                for port in ports:
                    info = dict(self.nmap[ip].udp(port))
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
    Using the output provided by unicorn scan,
    perform an exaustive scan using nmap.
    """
    def scan(self):
        self.nmap.scan(hosts=self.ipaddr, arguments=self.args)
        return self.nmap
