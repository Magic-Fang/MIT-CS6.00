# Problem 3.
# Write a function, called constrainedMatchPair which takes three arguments: a tuple
# representing starting points for the first substring, a tuple representing starting points for the second
# substring, and the length of the first substring. The function should return a tuple of all members
# (call it n) of the first tuple for which there is an element in the second tuple (call it k) such
# that n+m+1 = k, where m is the length of the first substring. Complete the definition
#
# def constrainedMatchPair(target, firstMatch,secondMatch):

import Set3_Problem2
def constrainedMatchPair(target, firstMatch, secondMatch):
    first_tuple = Set3_Problem2.subStringMatchExact(target, firstMatch)
    second_tuple = Set3_Problem2.subStringMatchExact(target, secondMatch)
    bingo_list = []
    for i in range(0, len(first_tuple)):
        # print('for i working')
        for j in range(0, len(second_tuple)):
            # print('for j working')
            if first_tuple[i] + len(firstMatch) + 1 == second_tuple[j]:
                # print('if working')
                bingo_list.append(first_tuple[i])
    return tuple(bingo_list)


firstMatch1 = 'a'
secondMatch1 = 'b'
target1 = 'acbooooacboooaffboooaboooafb'
length1 = 1
print('the answer for question 3 is ', constrainedMatchPair(target1, firstMatch1, secondMatch1))