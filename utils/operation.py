"""
Author: Alessio Greggi
Description:
Class to manage operations launched from console.
Operations are atomic shell script which executes a specific action.
The following class help you to check if the operation is still running,
or getting its output after finished.
"""

import subprocess
import traceback
from utils import variables as v

class Operation():

    """
    Constructor
    """
    def __init__(self, script_name, port):
        self.cmd = None
        self.script_name = script_name
        self.port = port

    """
    Retrieve current script name
    """
    def getName(self):
        return self.script_name

    """
    Retrieve attacking port
    """
    def getPort(self):
        return self.port

    """
    Run the script
    """
    def execute(self, host, port):
        try:
            self.cmd = subprocess.Popen(["/bin/sh", v.base_script + self.script_name, host, port], \
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
            stdout, stderr = self.cmd.communicate()
            return stdout, stderr
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
