"""
Author: Alessio Greggi
Description:
Class to control the application flow.
This allow you to have a console to manage the script,
executing available command such as status, show, etc..
"""

import cmd
import sys
import threading
import os

from utils import tcp_scan
from utils import udp_scan
from utils import operation
from utils import variables as v

class Controller(cmd.Cmd):
    prompt = v.PROMPT

    def __init__(self, host):

        super(Controller, self).__init__()

        self.operations = {}
        self.scans = {}
        self.tcp = None
        self.udp = None
        self.host = host
        self.thread_tcp = None
        self.thread_udp = None

        print(v.SHELL)

        # Scanning phase
        self.tcp = tcp_scan.TCPScan(host)
        self.udp = udp_scan.UDPScan(host)

        #thread_tcp = threading.Thread(target=tcp.scan)
        self.thread_tcp = threading.Thread(target=self.tcp.fullscan)
        self.thread_udp = threading.Thread(target=self.udp.scan)
        self.thread_tcp.setDaemon(True)
        self.thread_udp.setDaemon(True)
        self.thread_tcp.start()
        self.thread_udp.start()

        # Take track of scanning threads
        self.scans[v.TCP] = self.thread_tcp
        self.scans[v.UDP] = self.thread_udp


    """
    Find right protocol scripts.
    TODO: Actually the method find scripts only
    searching for protocol. Would be a great improvement
    create a map to allow the method to find all the scripts
    for the right protocol.
    """
    def findScripts(self, pattern):
        files = []
        for file in os.listdir(v.base_script):
            if file.startswith(pattern):
                files.append(file)
        return files


    """
    Perform the gathering against ports found.
    """
    def do_attack(self, _):
        'Perform the gathering against ports found.'
        # TCP attack
        tcp_results = self.tcp.result()
        for res in tcp_results:
            port = res[0]
            proto = res[1]
            scripts = self.findScripts(proto)
            for script in scripts:
                op = operation.Operation(script, str(port))
                operation_name = script + "-" + str(port)
                self.operations[operation_name] = op
                print(operation_name)

                thread = threading.Thread(target=op.execute, args=[self.host, str(port)])
                thread.setDaemon(True)
                thread.start()
        # UDP attack
        udp_results = self.udp.result()
        for res in udp_results:
            port = res[0]
            proto = res[1]
            scripts = self.findScripts(proto)
            for script in scripts:
                op = operation.Operation(script, str(port))
                operation_name = script + "-" + str(port)
                self.operations[operation_name] = op
                print(operation_name)

                thread = threading.Thread(target=op.execute, args=[self.host, str(port)])
                thread.setDaemon(True)
                thread.start()
        print()


    """
    Method to execute commands for debugging.
    """
    def do_exec(self, script_name):
        'Execute script manually.'
        op = operation.Operation(script_name)
        self.operations[script_name] = op

        thread = threading.Thread(target=op.execute, args=[self.host, port])
        thread.setDaemon(True)
        thread.start()
        print()


    """
    List available scripts.
    For debugging.
    """
    def do_list(self, _):
        'List available scripts.'
        files = os.listdir(v.base_script)
        for file in files:
            print(file)
        print()


    """
    Check status of running operations.
    """
    def do_status(self, _):
        'Show the status of pending operations running for the reconnaissance.'
        print("[SCANNING]")
        for scan in self.scans:
            if not self.scans[scan].isAlive():
                print(scan + ": " + v.GREEN + "completed" + v.RST)
            else:
                print(scan + ": " + v.RED + "running" + v.RST)
        print()
        print("[OPERATIONS]")
        if len(self.operations) < 1:
            print("...")
        for ops in self.operations:
            if not self.operations[ops].isAlive():
                print(ops + ": " + v.GREEN + "completed" + v.RST)
            else:
                print(ops + ": " + v.RED + "running" + v.RST)
        print()


    """
    Get output of the process.
    """
    def do_show(self, script_name):
        'Show the output of the selected operation. Usage: show [ scan | operation ].'
        if script_name == v.TCP:
            print(self.tcp.getOutput())
        elif script_name == v.UDP:
            print(self.udp.getOutput())
        elif script_name in self.operations:
            print("---------------- " + script_name + " ----------------")
            if not self.operations[script_name].isAlive():
                out, err = self.operations[script_name].getOutput()
                print(out.decode('utf-8'))

                # Check if stderr is empty
                if not err == b'':
                    print("[ERROR]")
                    print(err.decode('utf-8'))
            else:
                print("Process is still running. Cannot access its stdout.")
            print("-----------------------------------------------------")
        else:
            print("Ununderstandable command!")
        print()


    """
    Auticompletion for show command.
    """
    def complete_show(self, text, line, begidx, endidx):
        'Help you listing the available scripts to be shown.'
        avail_scripts = []
        hints = []
        # Prepare available scripts list
        avail_scripts.append(v.TCP)
        avail_scripts.append(v.UDP)
        for ops in self.operations:
            avail_scripts.append(ops)

        # Filter scripts that match research
        for script in avail_scripts:
            if text in script:
                hints.append(script)
        if len(hints) == 1:
            completion = hints[0]
            return [ completion ]
        else:
            return hints


    """
    Quit the program.
    """
    def do_quit(self, _):
        'Quit the program.'
        sys.exit(0)
