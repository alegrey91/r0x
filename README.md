# r0x

#  ![logo](r0x.jpg)


[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
## Introduction

**r0x** is an automated enumeration script written in python.
It uses **nmap** to discover opened ports and then enumerate them using a set of scripts provided under the `scripts/` directory.

To improve the detail of information retrievable you can just add some scripts under the dedicated directory and start **r0x** to catch them using a smart nomenclature as described below.

Ex. If we want to introduce a new script to automatically retrieve the `/robots.txt` file from a web server, we have just to create a script with a name as `http-robots` and make it executable.

As you can see, the first part of the name (`http`) indicates the protocol we are going to enumerate.

The rest of the name is left free to the author's imagination 😎.

Inside the script we can place the following command:

`curl http://$1/robots.txt`

where `$1` will be the ip address passed by **r0x**.



**P.S.** The name is due to a collegue of mine, considered one of the last real hacker out there.
His name is **Rosario** (aka **r0x**).



## Installation

To install the **r0x** and make it work, you neet at first to clone the repo:

`git clone https://github.com/alegrey91/r0x.git && cd r0x/`

And finally you can launch the dependencies installation:

`sudo pip3 install -r requirements.txt`

Once you finished the installation you are ready to launch **r0x** against your target.



## Usage

First of all, **r0x** is very easy to use.

```bash
$ ./r0x.py -h
          ___          
    _ __ / _ \__  __   
   | '__| | | \ \/ /   
   | |  | |_| |>  <    
   |_|   \___//_/\_\   
           by alegrey91

usage: r0x.py [-h] host

r0x is a network scanner for pentesting.

positional arguments:
  host        Host ip address(es)

optional arguments:
  -h, --help  show this help message and exit
```

Syntax is very similar to **nmap**. 

You can choose between TIMING and PORT parameters (equally to nmap).



## Scope

The scope of this project is to automate the scanning process and the information gathering during CTFs 💻😆.
