#!/usr/bin/env python3

__author__ = "alegrey91"
__version__ = "0.9.9"

import argparse
import signal
import sys
from utils import controller

def banner():
    print("\033[0m          ___          \033[0m")
    print("\033[0m    _ __ / _ \__  __   \033[0m")
    print("\033[93m   | '__| | | \ \/ /   \033[0m")
    print("\033[33m   | |  | |_| |>  <    \033[0m")
    print("\033[91m   |_|   \___//_/\_\   \033[0m")
    print("           version: {}".format(__version__))
    print("           by {}".format(__author__))
    print()

def signal_handler(sig, frame):
    print('Ctrl+C pressed.')
    sys.exit(0)

if __name__ == "__main__":

    banner()
    signal.signal(signal.SIGTERM, signal_handler)

    # Argument parsing
    parser = argparse.ArgumentParser(description='r0x is an automated enumeration tool.')
    parser.add_argument("host",
            type=str,
            help="Host ip address(es)")
    args = parser.parse_args()

    # Variables definition
    host = args.host

    ctl = controller.Controller(host)
    ctl.cmdloop()
