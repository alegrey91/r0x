#!/usr/bin/env python3

import subprocess

class Operation():

    """
    Constructor
    """
    def __init__(self, script_name):
        self.cmd = None
        self.script_name = script_name

    """
    Retrieve current script name
    """
    def getCmdtName(self):
        return self.script_name

    """
    Run the script
    """
    def execute(self, host):
        self.cmd = subprocess.run(["scripts/" + self.script_name, host], \
                               shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#        try:
#            outs, errs = cmd.communicate(timeout=15)
#        except TimeoutExpired:
#            proc.kill()
#            outs, errs = cmd.communicate()
#            print(outs)

    """
    Retrieve the output of the command
    """
    def print_output(self):
        return self.cmd.stderr.decode('utf-8'), self.cmd.stdout.decode('utf-8')

    """
    Check if process is still running
    """
    def isAlive(self):
        try:
            if self.cmd.poll() is None:
                return False
            else:
                return True
        except Exception:
            return False
