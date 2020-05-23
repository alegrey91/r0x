# r0x

#  ![logo](r0x.jpg)

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

## Introduction

**r0x** is an automated enumeration tool written in python.
It uses **nmap** to discover open ports and then enumerate them using a set of commands provided under the `scripts/` directory.

The main feature of **r0x** is the interactiveness. After started, **r0x** provide a simple menu where you can check the scripts **status**, **list** them, and **show** their output.

For example, using the command `show script_name` you can easly watch the output and take your time to analyze it (in the meantime that the rest of the scripts finish their execution).

Here, I provided a short video that show the basic behavior of **r0x** in a demo environment:

[![asciicast](https://asciinema.org/a/N0s2TeTfL34xIDrqrcyvyBz8n.png)](https://asciinema.org/a/N0s2TeTfL34xIDrqrcyvyBz8n)

#### Dedication

The name is due to a collegue of mine, considered one of the last real hackers out there.
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
sudo ./r0x.py -h
		  ___          
    _ __ / _ \__  __   
   | '__| | | \ \/ /   
   | |  | |_| |>  <    
   |_|   \___//_/\_\   
           version: 0.9.5
           by alegrey91

usage: r0x.py [-h] host

r0x is a network scanner for pentesting.

positional arguments:
  host        Host ip address(es)

optional arguments:
  -h, --help  show this help message and exit
```

To start to scan your target, just type the following command: `sudo ./r0x.py target.ip`.



## Contribution (scripts)

To increment the details of information retrievable by **r0x** is quite simple.

You can just add some scripts under the dedicated directory and start **r0x** to catch them using a smart nomenclature as described below.

*Ex.* If we want to introduce a new script to automatically retrieve the `/robots.txt` file from a web server, we have just to create a script with a name as `http-robots` and make it executable.

As you can see, the first part of the name (`http`) indicates the protocol we are going to enumerate.

The rest of the name is left free to the author's imagination 😎.

Inside the script we can place the following command:

`curl http://$1:$2/robots.txt`

where `$1` is the **ip address**, and `$2` the **port number**, both passed by **r0x** as script arguments.



## Scope

The scope of this project is to automate the scanning process and the information gathering during CTFs 💻😆.
