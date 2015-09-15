#!/usr/bin/X11/python
#print all prime number between 2 and 100

import math


for num in range(2,100):
    
    for sub in range(2,int(math.ceil(math.sqrt(num)))):
        if(num%sub == 0):
            break
    else:
        print num,
            
print ""
print "byebye!"
