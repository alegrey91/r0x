FROM kalilinux/kali-rolling

COPY . /root/r0x

# Install legion dependencies.
RUN apt-get update
RUN apt-get install -y \
        curl \
        dirb \
        dnsrecon \
        dnsutils \
        enum4linux \
        gobuster \
        hydra \
        netcat \
        nfs-common \
        nikto \
        nmap \
        ntp \
        python3 \
        python3-ldapdomaindump \
        python3-pip \
        smbclient \
        smbmap \
        snmpcheck

# Start the installation phase.
RUN cd /root/r0x
RUN pip3 install -r /root/r0x/requirements.txt

WORKDIR /root/r0x
