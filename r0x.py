#!/usr/bin/env python3

__author__ = "alegrey91"

import nmap as nm
import argparse
import threading
import signal
import sys
from utils import tcp_scan
from utils import udp_scan

def banner():
    print("          ___          ") 
    print("    _ __ / _ \__  __   ") 
    print("   | '__| | | \ \/ /   ") 
    print("   | |  | |_| |>  <    ") 
    print("   |_|   \___//_/\_\   ")
    print("           by {}".format(__author__))
    print()

def signal_handler(sig, frame):
    print('Ctrl+C pressed.')
    sys.exit(0)

default_arguments = "-n -Pn -sS -sV -T{} "

if __name__ == "__main__":

    banner()
    signal.signal(signal.SIGINT, signal_handler)

    # Argument parsing
    parser = argparse.ArgumentParser(description='r0x is a network scanner for pentesting.')
    parser.add_argument("host",
            type=str, 
            help="Host ip address(es)")
    parser.add_argument("-T", 
            "--timing", 
            type=int, 
            help="Set scan timing -T 0-5. \
                    Default 4", 
            default=3, 
            required=False)
    parser.add_argument("-p",
            "--port", 
            type=str,
            help="Select ports to scan. -p <port ranges>: Only scan specified ports \
                Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9", 
            required=False)
    args = parser.parse_args()

    # Make some checks/actions for arguments provided.
    if args.port:
        default_arguments += "-p{} ".format(args.port)
    if args.timing:
        default_arguments = default_arguments.format(args.timing)

    # Variables definition
    host = args.host
    arguments = default_arguments
    
    print("nmap {}{}".format(arguments, host))
    print()

    # Scanning phase
    print("[TCP]")
    tcp = tcp_scan.TCPScan(host, arguments)
    tcp.scan()

    print("[UDP]")
    udp = udp_scan.UDPScan(host)
    udp.scan()

    #thread = threading.Thread(target=udp.scan)
    #thread.start()
    #print(udp_ports)
