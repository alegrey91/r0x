#!/usr/bin/env python3

import cmd
import sys
import threading

from utils import tcp_scan
from utils import udp_scan
from utils import operation

class Controller(cmd.Cmd):
    prompt = "⮡  "

    def __init__(self, host):

        self.operations = {}
        self.scans = {}
        self.tcp = None
        self.udp = None
        self.host = host

        super(Controller, self).__init__()

        print("[r0x-shell]")
        # Scanning phase
        self.tcp = tcp_scan.TCPScan(host)
        self.udp = udp_scan.UDPScan(host)

        #thread_tcp = threading.Thread(target=tcp.scan)
        thread_tcp = threading.Thread(target=self.tcp.fullscan)
        thread_udp = threading.Thread(target=self.udp.scan)
        thread_tcp.setDaemon(True)
        thread_udp.setDaemon(True)
        thread_tcp.start()
        thread_udp.start()

        # Take track of scanning threads
        self.scans["tcp_scan"] = thread_tcp
        self.scans["udp_scan"] = thread_udp

    """
    Method to execute commands for tests
    """
    def do_exec(self, script_name):
        op = operation.Operation(script_name)
        self.operations[script_name] = op
        print(self.operations)
        op.execute(self.host)


    def do_status(self, _):
        'Show the status of pending operations running for the reconnaissance.'
        print("[SCANNING]")
        for scan in self.scans:
            if not self.scans[scan].isAlive():
                print(scan + ": \033[32mcompleted\033[0m")
            else:
                print(scan + ": \033[31mrunning\033[0m")

        print("[OPERATIONS]")
        for ops in self.operations:
            if not self.operations[ops].isAlive():
                print(self.operations[ops].getCmdtName() + ": \033[32mcompleted\033[0m")
            else:
                print(self.operations[ops].getCmdtName() + ": \033[31mrunning\033[0m")
        print()


    def do_show(self, script_name):
        'Show the output of the selected operation. Usage: show [ scan | operation ].'
        if script_name == "tcp_scan":
            print(self.tcp.print_output())
        elif script_name == "udp_scan":
            print(self.udp.print_output())
        else:
            print("---------------- " + script_name + " ----------------")
            err, out = self.operations[script_name].print_output()
            print(out)
            print(err)
        print()


    def do_quit(self, _):
        'Quit the program.'
        sys.exit(0)
