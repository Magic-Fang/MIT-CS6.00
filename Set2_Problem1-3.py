# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:51:37 2017

@author: Zhou Fang

Problem 1-2

Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets, 
by finding solutions to the Diophantine equation. list the combinations of 
6, 9 and 20 packs of McNuggets you need to buy in order to get each of the 
exact amounts.Given that it is possible to buy sets of 50, 51, 52, 53, 54 
or 55 McNuggets by combinations of 6, 9 and 20 packs, show that it is possible
 to buy 56, 57,…, 65 McNuggets. In other words, show how, given solutions 
 for 50-55, one can derive solutions for 56-65.
 
Problem 3

Write an iterative program that finds the largest number of McNuggets that
cannot be bought in exact quantity.

"""
maxium=1000        #the max number of mcnuggets I want to test
mcnuggets_plan=7    #the number of mcnuggets planned to buy
mcnuggets_cannot=[]
i=0
while mcnuggets_plan<=maxium:
    cof_six=0
    cof_nine=0
    cof_twn=0
    while 20*cof_twn<=mcnuggets_plan:        # try to figure out function 20x + 9y + 6z = n
        while 20*cof_twn+9*cof_nine <= mcnuggets_plan:
            while 6*cof_six + 9*cof_nine + 20*cof_twn <= mcnuggets_plan:
                if 6*cof_six + 9*cof_nine + 20*cof_twn == mcnuggets_plan:
                    print ('%d McNuggets = %d six + %d nine + %d twn'%(mcnuggets_plan,cof_six,cof_nine,cof_twn))
                    break
                cof_six=cof_six+1
            if 6*cof_six + 9*cof_nine + 20*cof_twn == mcnuggets_plan:
                break
            cof_six=0
            cof_nine=cof_nine+1
        if 6*cof_six + 9*cof_nine + 20*cof_twn == mcnuggets_plan:
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