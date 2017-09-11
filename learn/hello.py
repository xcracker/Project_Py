#!/usr/bin/python  
#coding=utf-8
import socket
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner):
    if 'vsFTPd' in banner:
        print '[+] vsVTPd is vulnerable.'
    elif 'FreeFloat Ftp Server' in banner:
        print '[+] FreeFloat Ftp Server.'
    elif 'condition':
        
        

