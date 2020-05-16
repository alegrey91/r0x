#!/usr/bin/env python3

import cmd
import sys
import threading

from utils import tcp_scan
from utils import udp_scan
from utils import operation

class Controller(cmd.Cmd):
    prompt = "⮡  "
    operations = []

    def __init__(self, host):

        super(Controller, self).__init__()

        print("[r0x-shell]")
        # Scanning phase
        tcp = tcp_scan.TCPScan(host)
        udp = udp_scan.UDPScan(host)

        thread_tcp = threading.Thread(target=tcp.scan)
        thread_udp = threading.Thread(target=udp.scan)
        thread_tcp.setDaemon(True)
        thread_udp.setDaemon(True)
        thread_tcp.start()
        thread_udp.start()

        self.operations.append(operation.Operation())
        self.operations.append(operation.Operation())

    def do_status(self, _):
        for ops in self.operations:
            print("status: " + ops.getOutput())

    def do_check(self, script_name):
        print(script_name)

    def do_quit(self, _):
        sys.exit(0)
