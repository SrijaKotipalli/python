# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:47:25 2022

@author: Srija 
"""
#Decision Control Structures program explanation
#simple if program
n=int(input("enter a number"))
if(n==0):
    print("positive number")
    
    
    #if-else program
S=int(input("enter a number"))
if(S>0):
    print("positive number")
else:
    print("negative number")

#nested-if program
#largest number
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if(a>b):
    if(a>c):
        print("a is large")
    else:
        print("c is large")
elif(b>c):
        print("b is large")
else:
        print("c is large")
        
#if-ellif-else program
#Relation between two numbers
p=int(input("enter p value"))
q=int(input("enter q value"))
if(p==q):
    print("both are equal")
elif(p>q):
    print("p is large")
else:
    print("q is largest")
    

