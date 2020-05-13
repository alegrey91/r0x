#!/usr/bin/env python3


import cmd, os, sys

class Status(cmd.Cmd):
    into = "r0x Shell"
    prompt = "(r0x)> "
#    path = os.path.abspath("scripts/")

    def do_status(self, _):
        print("")

    def do_check(self, script_name):
        print(script_name)

    def do_exit(self, _):
        sys.exit(0)

if __name__ == '__main__':
    Status().cmdloop()
