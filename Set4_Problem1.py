# Problem 1.
# Write a function, called nestEggFixed, which takes four arguments: a salary, a percentage of your
# salary to save in an investment account, an annual growth percentage for the investment account,
# and a number of years to work. This function should return a list, whose values are the size of
# your retirement account at the end of each year, with the most recent year’s value at the end of
# the list.
# Complete the implementation of:
# def nestEggFixed (salary, save, growthRate, years):
# Write your code in the appropriate place in the ps4.py template. To test your function, run the
# test cases in the test function testNestEggFixed(). You should add additional test cases to this
# # function to further test your code.
#
#                  Retirement fund
# End of year 1    F[0] = salary * save * 0.01
# End of year 2    F[1] = F[0] * (1 + 0.01 * growthRate) + salary * save * 0.01
# End of year 3    F[2] = F[1] * (1 + 0.01 * growthRate) + salary * save * 0.01


def nestEggFixed_integer (salary, save, growthRate, years):
    if years < 1:
        print('years should be at least 1 year')
    elif years == 1:
        return salary*save*0.01
    else:
        return nestEggFixed_integer(salary, save, growthRate, years-1)*(1+0.01*growthRate)+salary*save*0.01

def nestEggFixed (salary, save, growthRate, years):
    if years < 1:
        print('years should be at least 1 year')
    elif years == 1:
        getherlist1 = [salary*save*0.01]
        return getherlist1
    else:
        getherlist = nestEggFixed(salary, save, growthRate, years-1)
        newyear = getherlist[years-2]*(1+0.01*growthRate)+salary*save*0.01
        getherlist.append(newyear)
        return getherlist

def testNestEggFixed():
    salary = int(input('input the value of salary: '))
    save = int(input('input the value of save: '))
    growthRate = int(input('input the value of growthrate: '))
    years = int(input('input the value of years: '))
    print(nestEggFixed_integer(salary, save, growthRate, years))
    print(nestEggFixed(salary, save, growthRate, years))


# testNestEggFixed()

#
# Problem 2.
# Write a function, called nestEggVariable, which takes three arguments: a salary (salary), a percentage of your
# salary to save (save), and a list of annual growth percentages on investments (growthRates). The length of the
# last argument defines the number of years you plan to work; growthRates[0] is the growth rate of the first year,
# growthRates[1] is the growth rate of the second year, etc. (Note that because the retirement fund’s initial
# value is 0, growthRates[0] is, in fact, irrelevant.) This function should return a list, whose values are the
# size of your retirement account at the end of each year.
# Complete the implementation of:
# def nestEggVariable(salary, save, growthRates):


def nestEggVariable(salary, save, growthRates):
    years = len(growthRates)
    if years < 1:
        print('years should be at least 1 year')
    elif years == 1:
        getherlist1 = [salary*save*0.01]
        return getherlist1
    else:
        getherlist = nestEggFixed(salary, save, growthRates[years-2], years-1)
        newyear = getherlist[years-2]*(1+0.01*growthRates[years-1])+salary*save*0.01
        getherlist.append(newyear)
        return getherlist

def testNestEggVariable():
    salary = int(input('input the value of salary: '))
    save = int(input('input the value of save: '))
    growthRates = eval(input('input a list of growthrate: '))
    print(growthRates)
    print(nestEggVariable(salary, save, growthRates))

#testNestEggVariable()


# Problem 3.
# Write a function, called postRetirement, which takes three arguments: an initial amount of money in your
# retirement fund (savings), a list of annual growth percentages on investments while you are retired
# (growthRates), and your annual expenses (expenses). Assume that the increase in the investment account
# savings is calculated before subtracting the annual expenditures (as shown in the above table). Your
# function should return a list of fund sizes after each year of retirement, accounting for annual expenses
# and the growth of the retirement fund. Like problem 2, the length of the growthRates argument defines
# the number of years you plan to be retired.


def postRetirement(savings, growthRates, expenses):
    years = len(growthRates)
    if years < 1:
        return savings
    elif years == 1:
        getherlist1 = [savings*(1+0.01*growthRates[0])-expenses]
        return getherlist1
    else:
        getherlist = postRetirement(savings, growthRates[:(years-1)], expenses)
        newyear = getherlist[years-2]*(1+0.01*growthRates[years-1]) - expenses
        getherlist.append(newyear)
        return getherlist



def testPostRetirement():
    savings = nestEggFixed_integer(18000, 10, 0.01, 30)
    growthRates = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    expenses = 5000
    remainedSavings = postRetirement(savings, growthRates, expenses)
    print(remainedSavings)

#testPostRetirement()


# Problem 4.
# Write a function, called findMaxExpenses, which takes five arguments: a salary
# (salary), a percentage of your salary to save (save), a list of annual growth percentages on
# investments while you are still working (preRetireGrowthRates), a list of annual growth percentages
# on investments while you are retired (postRetireGrowthRates), and a value for epsilon (epsilon).
# As with problems 2 and 3, the lengths of preRetireGrowthRates and postRetireGrowthRates determine
# the number of years you plan to be working and retired, respectively.
# Use the idea of binary search to find a value for the amount of expenses you can withdraw each year ：
# def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon):


def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon):
    preyears = len(preRetireGrowthRates)
    postyears = len(postRetireGrowthRates)
    savinglist_pre = nestEggVariable(salary, save, preRetireGrowthRates)
    saving_pre = savinglist_pre[preyears-1]
    print(saving_pre)
    i = 0    # the initial value is not important
    upperbound = saving_pre
    lowbound = 0
    expenses = 0
    while i <= 500:
        i += 1
        print('This is ', i, ' th recursion. And expenses is', expenses)
        expenses = (upperbound + lowbound)/2
        remainlist = postRetirement(saving_pre, postRetireGrowthRates, expenses)
        remain = remainlist[postyears-1]
        if abs(remain) < epsilon:
            break
        elif remain > 0:
            lowbound = (lowbound + expenses)/2
        else:
            upperbound = (upperbound + expenses)/2
    return expenses

def testFindMaxExpenses():
    preRetireGrowthRates = [1]*40
    postRetireGrowthRates = [1]*20
    print('begin')
    print(findMaxExpenses(10000, 15, preRetireGrowthRates, postRetireGrowthRates, 1))

testFindMaxExpenses()