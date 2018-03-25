# The function get_word_score should accept a string of lowercase letters as input (a word) and return the
# integer score for that word, using the game's scoring rules.
# Fill in the code for get_word_score in ps5.py:
# def get_word_score(word, n): """
#       Returns the score for a word. Assumes the word is a
#       valid word.
#           The score for a word is the sum of the points for letters
#           in the word, plus 50 points if all n letters are used on
#           the first go.
#           Letters are scored as in Scrabble; A is worth 1, B is
#           worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
#       word: string (lowercase letters)
#       n: integer (maximum hand size; i.e., hand size required for additional
#   points)
#       returns: int >= 0
# """
# You may assume that the input word is always either a string of lowercase letters, or the empty string "".
# You will want to use the SCRABBLE_LETTER_VALUES dictionary defined at the top of ps5.py. You should not
# change its value.
# Do not assume that there are always 7 letters in a hand! The parameter n is the number of letters required
# for a bonus score (the maximum number of letters in the hand).


SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 3, 'g': 2, 'h': 3, 'i':1, 'j':2, 'k':1,
                          'l':2, 'm':3, 'n':1, 'o':2, 'p':3, 'q':1, 'r':2, 's':1, 't':2, 'u':3, 'v':1, 'w':2,
                          'x':1, 'y':2, 'z':3}


def get_word_score(word, n):
    if len(word) == n:
        score = 50
    else:
        score = 0
    for letter in word:
        score = score + SCRABBLE_LETTER_VALUES[letter]
    return score


word = 'ninewords'
n = 9
print(get_word_score(word, n))

