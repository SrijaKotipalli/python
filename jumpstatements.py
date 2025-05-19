# -*- coding: utf-8 -*-
"""
Created on Thu May 26 18:15:44 2022

@author: Srija 
"""

#unconditional jumpstatements
#break
i=1
while(i<=10):
    print (i)
    if(i==5):
        break
    i=i+1
print("loop terminated")

#continue
for j in range(1,10):
    if(j==6):
        continue
    print(j)
print("loop terminated")
