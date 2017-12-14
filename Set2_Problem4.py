# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:51:37 2017

@author: Zhou Fang

Problem 4
Assume that the variable packages is bound to a tuple of length 3, 
the values of which specify the sizes of the packages, ordered from 
smallest to largest. Write a program that uses exhaustive search to
find the largest number (less than 200) of McNuggets that cannot 
be bought in exact quantity.


"""
packages=(6,9,20)   #change the different package combination here
maxium=200       #the max number of mcnuggets I want to test
mcnuggets_plan=7    #the number of mcnuggets planned to buy
mcnuggets_cannot=[]
i=0
while mcnuggets_plan<=maxium:
    cof_six=0
    cof_nine=0
    cof_twn=0
    while packages[2]*cof_twn<=mcnuggets_plan:        # try to figure out function 20x + 9y + 6z = n
        while packages[2]*cof_twn+packages[1]*cof_nine <= mcnuggets_plan:
            while packages[0]*cof_six + packages[1]*cof_nine + packages[2]*cof_twn <= mcnuggets_plan:
                if packages[0]*cof_six + packages[1]*cof_nine + packages[2]*cof_twn == mcnuggets_plan:
                    #print ('%d McNuggets = %d six + %d nine + %d twn'%(mcnuggets_plan,cof_six,cof_nine,cof_twn))
                    break
                cof_six=cof_six+1
            if packages[0]*cof_six + packages[1]*cof_nine + packages[2]*cof_twn == mcnuggets_plan:
                break
            cof_six=0
            cof_nine=cof_nine+1
        if packages[0]*cof_six + packages[1]*cof_nine + packages[2]*cof_twn == mcnuggets_plan:
            break
        cof_nine=0
        cof_six=0
        cof_twn=cof_twn+1
    else: 
        mcnuggets_cannot.append(mcnuggets_plan)
        i=i+1
    mcnuggets_plan=mcnuggets_plan+1
print('In range of 6-',maxium,', this is the list of McNuggets number \
      which cannot be brought\n',mcnuggets_cannot[:])
print('Therefore, if the maxium number you set is big enough, the correct result \
for the largest number of McNuggets that cannot be bought should be ',mcnuggets_cannot[i-1])