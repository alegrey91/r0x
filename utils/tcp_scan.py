"""
Author: Alessio Greggi
Description:
Class to automamate tcp scanning process.
"""
import nmap as nm

NMAPSCAN = "-n -Pn -T4 -sS "

class TCPScan:

    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.args = NMAPSCAN
        self.nmap = nm.PortScanner()


    """
    Print formatted output.
    """
    def getOutput(self):
        for ip in self.nmap.all_hosts():
            ports = self.nmap[ip].all_tcp()
            print("[TCP]")
            print("PORT\tSTATUS\tPROTO\tVERSION")
            if len(ports) != 0:
                for port in ports:
                    info = dict(self.nmap[ip].tcp(port))
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
        self.nmap.scan(hosts=self.ipaddr, arguments=self.args)
        return self.nmap


    """
    Scan using a basic SYN scan.
    """
    def fullscan(self):
        self.args += "-p- "
        self.nmap.scan(hosts=self.ipaddr, arguments=self.args)
        return self.nmap
