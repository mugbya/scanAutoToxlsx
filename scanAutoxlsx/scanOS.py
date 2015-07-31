#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-07-22 13:34:27
#  

import os,sys 
import nmap
from outToXlsx import createFile
from handlerData import wirteContent

try:
    nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)


def scanOS(filename, ip, rows):
    nm.scan(hosts=ip, arguments='-sT  -f -O  --min-hostgroup 10 --max-hostgroup 50 ')

    # host = nm.all_hosts()  # if it's iphone ,no value
    if nm.all_hosts():
        host = nm.all_hosts()[0]
        wirteContent(filename+'.xlsx', host, 'C'+str(rows))
        if nm[host].all_protocols():
            for proto in nm[host].all_protocols():
                if 'osclass' == proto:
                    wirteContent(filename+'.xlsx', nm[host][proto][0]['type'], 'E'+str(rows))
                if 'osmatch' == proto:
                    wirteContent(filename+'.xlsx', nm[host][proto][0]['name'], 'D'+str(rows))
                if 'tcp'== proto:
                    lport = nm[host][proto].keys()
                    lport = sorted(lport)
                    for port in lport:
                        wirteContent(filename+'.xlsx', port, 'F'+str(rows))
                        wirteContent(filename+'.xlsx', nm[host][proto][port]['state'], 'G'+str(rows))
                        wirteContent(filename+'.xlsx', nm[host][proto][port]['name'], 'H'+str(rows))
                        rows += 1
        else:
            rows += 1
    else:
        print(ip + 'is iphone ')
        rows += 1
    return rows


def fileHandler():
    filename = sys.argv[1]
    rows = 8
    createFile(filename+'.xlsx')
    with open(filename, 'r') as f:
        for line in f.readlines():
            if 'scan report for' in line:
                ip = line.rsplit(None, 1)[-1]
                rows = scanOS(filename, ip, rows)

def scan():
    fileHandler()

if __name__=='__main__':
    scan()
