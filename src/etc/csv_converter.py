# -*- coding: utf-8 -*-

import csv
import socket
import netaddr

def inttoip(ip):
    return socket.inet_ntoa(hex(ip)[2:].zfill(8).decode('hex'))

with open("../text-files/ip_loc.csv") as csvfile:  # megnyitás olvasásra
    readCSV = csv.reader(csvfile, delimiter=',')
    
    with open('../text-files/ip_location.csv', 'w') as fp:
        writeCSV = csv.writer(fp, delimiter=',')

        i = 0  # 218148
        for row in readCSV:
            if i == 218148:
                break
            
            data = [[int(netaddr.IPAddress(row[0])), int(netaddr.IPAddress(row[1])), row[2]]]
            writeCSV.writerows(data)
            
            i += 1
        
print "kész"
