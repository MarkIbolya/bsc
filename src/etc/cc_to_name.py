# -*- coding: utf-8 -*-

import csv

f = open("../text-files/country_codes.txt").read().split("\n")
i=0

with open("../text-files/ip_location_backup.csv") as csvfile:  # megnyitás olvasásra
    readCSV = csv.reader(csvfile, delimiter=',')
    
    with open("../text-files/ip_loc_modified.csv","w+") as fp:  # megnyitás olvasásra
        writeCSV = csv.writer(fp, delimiter=',')
        

        for ips in readCSV:
            for line in f:
                if line.split(";")[1]==ips[2]:
                    data = [[ips[0],ips[1],line.split(";")[0]]]
                    print data
                    writeCSV.writerows(data)