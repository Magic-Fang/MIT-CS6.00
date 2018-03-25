# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def play_ghost():
    print('Welcome to Ghost! \n')
    turn = -5
    number = 0
    status = True
    fragmentlist = []
    while status:
            player = (turn + 15)//10
            print('Turn of player ', player, '\nThis player says: ', end='')
            letter = input()
            if letter in string.ascii_letters:
                letter.lower()
                if len(letter) != 1:
                    print('Input should be one letter')
                else:
                    fragmentlist.append(letter)
                    fragment = ''.join(fragmentlist)
                    for word in wordlist:
                        if fragment == word:
                            print('Player ', player, ' loses because ', fragment, 'is a word')
                            return None
                    for word in wordlist:
                        if word.startswith(fragment):
                            number += 1
                            turn = -turn
                            print('\nCurrent fragment is', fragment)
                            break
                        else:
                            print('Player ', player, 'loses because no word begins with', fragment)
                            return None
            else:
                print('Input should be one letter')


play_ghost()