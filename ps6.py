# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#
import time
import random
import itertools

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5,
    'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4,
    'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"
words_points_dic = {}


def load_words():      # load the txt file
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


def get_words_to_points(word_list):
    global words_points_dic
    for word in word_list:
        score = get_word_score(word, HAND_SIZE)
        words_points_dic[word] = score


def get_frequency_dict(sequence):   # create a new dic in which contains the show-up times of letters in sequence
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:                    # create a new dic in which contains the show-up times of letters in sequence
        freq[x] = freq.get(x,0) + 1       # add 1 to the value which points to the key x
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    if len(word) == n:
        score = 50
    else:
        score = 0
    for letter in word:
        score = score + SCRABBLE_LETTER_VALUES[letter]
    return score



#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():         # hand is a dic; .keys return a list of the keys
        for j in range(hand[letter]):
            print(letter, end='')            # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n // 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]       # VOWELS & CONSONANT are pre-defined in the head of the file
        hand[x] = hand.get(x, 0) + 1                      # dic is not ordered, so we can add a pair directly
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand, word):     # hand is a dic while word is a string
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    for letter in word:
        if letter in hand:
            hand[letter] = hand.get(letter, 0) - 1
            if hand.get(letter, 0) == 0:
                del hand[letter]
    return hand

        #
# Problem #3: Test word validity


def is_valid_word(word, hand, words_points_dic):        # word_list is a list that contains all possible answer
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    if word not in words_points_dic:
        return False
    else:
        for letter in word:
            if letter in hand:
                hand[letter] = hand.get(letter, 0) - 1
                if hand.get(letter, 0) < 0:
                    return False
            else:
                return False
        return True

#
# Problem #4: Playing a hand


def play_hand(hand, words_points_dic):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    print('''The new game begins. Please enter a word constructed using the characters in the given hand.
              If you want to quit the game, enter a symbol '.' ''') # replace this with your code...
    valid_status = True
    total_score = 0
    time_total = 0
    while valid_status:
        print('Now, your hand is \n')
        display_hand(hand)
        input()
        time_begin = time.time()
        word = pick_best_word(hand.copy())
        time_end = time.time()
        time_cost = time_end - time_begin
        time_total = time_total + time_cost
        print('It cost %0.2f to provide a answer'%time_cost)
        if time_total >= 8:
            print('Total time exceeds 8 seconds, your score is', total_score)
            break
        print('You have %0.2f seconds remaining' % (8-time_total))
        if word == '.':
            print('Total score', total_score)
            break
        valid_status = is_valid_word(word, hand, words_points_dic)
        if not valid_status:
            print('Not correct!   Please enter again.')
            valid_status = True
        else:
            this_score = (get_word_score(word, HAND_SIZE))
            total_score = total_score + this_score
            print(word, ' earns', this_score, '. Total score is ', total_score)
            hand = update_hand(hand.copy(), word)
            if hand == {}:                # when there is no element in hand
                print('Total score', total_score)
                break
    print('Game finished with this hand!')
    return None


#
# Problem #5: Playing a game
# Make sure you understand how this code works!

def construt_combination_list(hand):
    """Part 1 is to transfer the hand(dic) to a hand_list which contains the letters
       Part 2 is to try all possible combination of word using all letters in hand_list and
              store the results into a combination_list
       Part 3 is to reconstruct the words and select those correct ones and add their score
              to the value of combination_dic
    """
    hand_list = []
    combination_list = []
    combination_dic = {}
    for letter in hand.keys():         # hand is a dic; .keys return a list of the keys
        for j in range(hand[letter]):
            hand_list.append(letter)                # Part 1 finished
    # print(hand_list)
    list_of_tuple_combination = itertools.permutations(hand_list, len(hand_list))
    for tuple_combination in list_of_tuple_combination:
        combination_str = ''
        for k in range(0, len(tuple_combination)):
            combination_str = combination_str + tuple_combination[k]
        combination_list.append(combination_str)    # Part 2 finished
    # print(len(combination_list))
    for key in combination_list:
        for word_length in range(1, len(hand_list)+1):
            status = is_valid_word(key[:word_length], hand.copy(), words_points_dic)
            # print(key[:word_length], status)
            if status:
                combination_dic[key[:word_length]] = get_word_score(key[:word_length], len(hand_list))
                                                    # Part 3 finished
    return combination_dic


#
def pick_best_word(hand):
    combination_dic = construt_combination_list(hand.copy())
    try:
        best_word = max(combination_dic.items(), key=lambda x: x[1])[0]
    except:
        best_word = '.'
    return best_word




def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    get_words_to_points(word_list)
    # print(words_points_dic)
    hand = deal_hand(HAND_SIZE)
    hand2 = hand.copy()
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), words_points_dic)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), words_points_dic)
            print
        elif cmd == 'e':
            break
        else:
            print("Invalid command.")