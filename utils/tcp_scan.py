"""
Author: Alessio Greggi
Description:
Class to automamate tcp scanning process.
"""
import nmap as nm

NMAPSCAN = "-n -Pn -T5 -sS "
NMAPDEEPSCAN = "-n -Pn -T5 -sS -sV -p {}"

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
        arg_ports = ""
        for ip in self.nmap.all_hosts():
            ports = self.nmap[ip].all_tcp()
            for i in range(0, len(ports)):
                if i == (len(ports) - 1):
                    arg_ports += str(ports[i])
                else:
                    arg_ports += str(ports[i]) + ","
            self.args = NMAPDEEPSCAN.format(arg_ports)
            self.nmap.scan(hosts=self.ipaddr, arguments=self.args)
        return self.nmap


    """
    Scan using a basic SYN scan.
    """
    def fullscan(self):
        self.args += "-p- "
        self.nmap.scan(hosts=self.ipaddr, arguments=self.args)
        arg_ports = ""
        for ip in self.nmap.all_hosts():
            ports = self.nmap[ip].all_tcp()
            for i in range(0, len(ports)):
                if i == (len(ports) - 1):
                    arg_ports += str(ports[i])
                else:
                    arg_ports += str(ports[i]) + ","
            self.args = NMAPDEEPSCAN.format(arg_ports)
            self.nmap.scan(hosts=self.ipaddr, arguments=self.args)
        return self.nmap


    """
    Get nmap results.
    """
    def result(self):
        results = []
        for ip in self.nmap.all_hosts():
            ports = self.nmap[ip].all_tcp()
            for port in ports:
                entry = []
                info = dict(self.nmap[ip].tcp(port))
                print(type(info['name']))
                print(type(info['state']))
                entry.append(port)
                entry.append(info['name'])
                results.append(entry)
        return results
