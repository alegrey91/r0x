# r0x

#  ![logo](r0x.jpg)



## Introduction

r0x is a network scanner written in python.
It uses the **python-nmap** library to retrieve informations about open ports on the target.
The purposes of this tool are the pluggable scripts wrote in bash.
These simple scripts contains just few raw of command such as: `nikto -host $host`.

P.S. The name is due to a collegue of mine, considered one of the last real hacker out there.
His name is **Rosario**.



## Installation

To install the **r0x** and make it work, you neet at first to clone the repo:

`git clone https://github.com/alegrey91/r0x.git && cd r0x/`

And finally you can launch the dependencies installation:

`sudo pip3 install -r requirements.txt`

Once you finished the installation you are ready to launch **r0x** against your target.



## Usage

First of all, **r0x** is very easy to use.

```
$ python r0x.py -h
          ___          
    _ __ / _ \__  __   
   | '__| | | \ \/ /   
   | |  | |_| |>  <    
   |_|   \___//_/\_\   
           by alegrey91

usage: r0x.py [-h] [-T TIMING] [-p PORT] host

r0x is a network scanner for pentesting.

positional arguments:
  host                  Host ip address(es)

optional arguments:
  -h, --help            show this help message and exit
  -T TIMING, --timing TIMING
                        Set scan timing -T 0-5. Default 4
  -p PORT, --port PORT  Select ports to scan. -p <port ranges>: Only scan specified ports Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
```

Syntax is very similar to **nmap**. 

You can choose between TIMING and PORT parameters (equally to nmap).



## Scope

The scope of this project is to automate the scanning process and the information gathering during CTFs 💻😆.