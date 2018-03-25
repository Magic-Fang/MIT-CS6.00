# Problem 4.
# Write a function, called subStringMatchExactlyOneSub which takes two arguments: a target
# string and a key string. This function should return a tuple of all starting points of matches of the key to
# the target, such that at exactly one element of the key is incorrectly matched to the target. Complete the definition
# def subStringMatchExactlyOneSub(target,key):

import Set3_Problem2
import Set3_Problem3
def subStringMatchExactlyOneSub(target, key):
    perfmacth_tuple = Set3_Problem2.subStringMatchExact(target, key)
    onenotmacth_list = []
    length = len(target)
    onenotmacth_tuple = ()
    for i in range(0, length+1):
        temptuple = Set3_Problem3.constrainedMatchPair(target, key[0:i], key[i+1:length])
        # the part matched positions for the key[i]-missing circumstance
        onenotmacth_tuple = tuple(set(onenotmacth_tuple + temptuple))
        # add the part matched lists together for each missing character
    answer_list = sorted(list(set(onenotmacth_tuple).difference(set(perfmacth_tuple))))
    return answer_list


target1 = 'fang likes play with fing, but fong does not like play with fing'
key1 = 'fang'
print('\n\n\nthe question 4 answer is ', subStringMatchExactlyOneSub(target1, key1))