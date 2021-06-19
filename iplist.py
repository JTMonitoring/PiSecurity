import os.path
from os import path
import sys

def getlist(path):
    iplist = []
    file = open(path, "r")
    lines = file.readlines()
    for line in lines:
        iplist.append(line)
    return iplist


def savelist(iplist):
    print("Checking if data file exists")
    if path.exists("src/ipdat.txt") == True:
        print("Data file exists. writing to file...")
        f = open("src/ipdat.txt", "r")
        for line in iplist:
            f.write(line)
        print("File has been sourced with IP addresses. Restart the Ping Monitor.")
    else:
        print("IP Data file dosent exist, creating...")
        
        
        f = open("src/ipdat.txt", "r")
        print("File has been created, writing IPs to file...")
        for line in iplist:
            f.write(line)
        print("File has been sourced with IP addresses. Restart the Ping Monitor.")
        f.close()

iplist = input("Path to IP text file> ")
savelist(iplist)

    