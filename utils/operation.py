#!/usr/bin/env python3

import subprocess
import traceback

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
    def getName(self):
        return self.script_name

    """
    Run the script
    """
    def execute(self, host):
        try:
            self.cmd = subprocess.Popen(["/bin/sh", "scripts/" + self.script_name, host], \
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except Exception as e:
            print(e)
            return False

    """
    Retrieve the output of the command
    """
    def getOutput(self):
        try:
            # Return stdout of the process
            return self.cmd.communicate()[0].decode("utf-8")
        except Exception as e:
            print(e)
            print("No output yet.")

    """
    Check if process is still running
    """
    def isAlive(self):
        try:
            # Check if process is alive
            if self.cmd.poll() is None:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
