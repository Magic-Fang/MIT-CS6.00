#
# Problem 1.
# Write two functions, called countSubStringMatch and countSubStringMatchRecursive that
# take two arguments, a key string and a target string. These functions iteratively and
# recursively count the number of instances of the key in the target string. You should
# complete definitions for
# def countSubStringMatch(target,key):
# and
# def countSubStringMatchRecursive (target, key):


def countSubStringMatch(target, key):        # iterative function
    position = 0
    count = 0                                # count is the number of times for which key shows up in my target
    perfcheck = target.find(key, 0, 1)   # check the data in the first position in my target
    if perfcheck >= 0:
        # print('perfcheck working')
        count = count + 1
    while position >= 0:
        position = target.find(key, position+1)
        # print('working')
        if position >= 0:
            count = count + 1
    return count


def countSubStringMatchRecursive(target, key):   # recursive function
    position = target.find(key)
    if position >= 0:                            # if position >= 0, there should be at least one keyword in the target
        count = 1 + countSubStringMatchRecursive(target[position+1:], key)
        # if key was found, start next check behind the position of key.
    else:
        count = 0
    return count


target1 = 'A good egg comes from a good chicken.'
key1 = 'g'
print(countSubStringMatch(target1, key1))
print(countSubStringMatchRecursive(target1, key1))

