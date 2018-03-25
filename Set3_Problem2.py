# Problem 2.
# Write the function subStringMatchExact. This function takes two arguments: a target string,
# and a key string. It should return a tuple of the starting points of matches of the key
# string in the target string, when indexing starts at 0. Complete the definition for
#
# def subStringMatchExact(target,key):
#
# For example,
# subStringMatchExact("atgacatgcacaagtatgcat","atgc")
# would return the tuple (5, 15).


def subStringMatchExact(target, key):
    position_list = []
    begin_point = 0
    temp_position = 0
    while temp_position >= 0:
        temp_position = target.find(key, begin_point)
        if temp_position >= 0:
            begin_point = temp_position + 1
            position_list.append(temp_position)
    position_tuple = tuple(position_list)
    return position_tuple


target1 = 'atgacatgcacaagtatgcat'
key1 = 'atgc'
print(subStringMatchExact(target1, key1))