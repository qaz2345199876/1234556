# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:19:22 2020

@author: cis-user
"""

print("解一元二次方程式:ax**2+bx+c=0")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
y=(-b+((b**2-4*a*c)**0.5))/2*a
x=(-b-((b**2-4*a*c)**0.5))/2*a
print(y,x)

