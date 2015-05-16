# -*- coding: utf-8 -*-
f = open("../text-files/passes.txt").read().split("\n")
o = open("../text-files/passwords.txt",'w+')
i=0
for acc_pass in f:
    try:
        o.write(str(acc_pass.split()[1])+"\n")
    except:
        pass
    i+=1
    #if i>100000:
       # break
print "done"