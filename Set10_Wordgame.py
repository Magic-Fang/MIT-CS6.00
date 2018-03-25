# Backend code for PS10

import random
import string
import itertools

# Global Constants
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 30
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '.': 0
}
HUMAN_SOLO = 0
HUMAN_VS_HUMAN = 1
HUMAN_VS_COMP = 2

WORDLIST_FILENAME = "/Users/fangzhou/PycharmProjects/problem_set4/words.txt"
words_points_dic = {}

def load_words():  # load the txt file
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(r'/Users/fangzhou/PycharmProjects/problem_set4/words.txt', 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_words_to_points(word_list):
    global words_points_dic
    for word in word_list:
        score = getWordScore(word)
        words_points_dic[word] = score


def getFrequencyDict(sequence):
    """
    Given a sequence of letters, convert the sequence to a dictionary of
    letters -> frequencies. Used by containsLetters().

    returns: dictionary of letters -> frequencies
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def getWordScore(word):
    """
    Computes the score of a word (no bingo bonus is added).

    word: The word to score (a string).

    returns: score of the word.
    """
    if len(word) == HAND_SIZE:
        score = 50
    else:
        score = 0
    for letter in word:
        score = score + SCRABBLE_LETTER_VALUES[letter]
    return score

#
# Problem 2: Representing a Hand
#

class Hand(object):
    def __init__(self, handSize, initialHandDict = None):
        """
        Initialize a hand.

        handSize: The size of the hand

        postcondition: initializes a hand with random set of initial letters.
        """
        num_vowels = handSize // 3
        if initialHandDict is None:
            initialHandDict = {}
            for i in range(num_vowels):
                x = VOWELS[random.randrange(0,len(VOWELS))]
                initialHandDict[x] = initialHandDict.get(x, 0) + 1
            for i in range(num_vowels, handSize):
                x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
                initialHandDict[x] = initialHandDict.get(x, 0) + 1
        self.initialSize = handSize
        self.handDict = initialHandDict
    def update(self, word):
        """
        Remove letters in word from this hand.

        word: The word (a string) to remove from the hand
        postcondition: Letters in word are removed from this hand
        """
        # TODO
        for letter in word:
            if letter in self.handDict:
                self.handDict[letter] = self.handDict.get(letter, 0) - 1
                if self.handDict.get(letter, 0) == 0:
                    del self.handDict[letter]
        return self.handDict

    def containsLetters(self, letters):
        """
        Test if this hand contains the characters required to make the input
        string (letters)

        returns: True if the hand contains the characters to make up letters,
        False otherwise
        """
        # TODO
        for letter in letters:
            if letter not in self.handDict:
                return False
        return True


    def isEmpty(self):
        """
        Test if there are any more letters left in this hand.

        returns: True if there are no letters remaining, False otherwise.
        """
        # TODO
        if self.handDict == {}:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Equality test, for testing purposes

        returns: True if this Hand contains the same number of each letter as
        the other Hand, False otherwise
        """
        # TODO
        for letter in other.handDict:
            if letter in self.handDict:
                if self.handDict[letter] == other.handDict[letter]:
                    pass
                else:
                    return False
            else:
                return False
        return True

    def __str__(self):
        """
        Represent this hand as a string

        returns: a string representation of this hand
        """
        string = ''
        for letter in self.handDict.keys():
            for j in range(self.handDict[letter]):
                string = string + letter + ' '
        return string

#
# Problem 3: Representing a Player
#

class Player(object):
    """
    General class describing a player.
    Stores the player's ID number, hand, and score.
    """
    def __init__(self, idNum, hand):
        """
        Initialize a player instance.

        idNum: integer: 1 for player 1, 2 for player 2.  Used in informational
        displays in the GUI.

        hand: An object of type Hand.

        postcondition: This player object is initialized
        """
        self.points = 0.
        self.idNum = idNum
        self.hand = hand

    def getHand(self):
        """
        Return this player's hand.

        returns: the Hand object associated with this player.
        """
        # TODO
        return self.hand

    def addPoints(self, points):
        """
        Add points to this player's total score.

        points: the number of points to add to this player's score

        postcondition: this player's total score is increased by points
        """
        # TODO
        self.points += points

    def getPoints(self):
        """
        Return this player's total score.

        returns: A float specifying this player's score
        """
        # TODO
        return self.points

    def getIdNum(self):
        """
        Return this player's ID number (either 1 for player 1 or
        2 for player 2).

        returns: An integer specifying this player's ID number.
        """
        # TODO
        return self.idNum

    def __cmp__(self, other):
        """
        Compare players by their scores.

        returns: 1 if this player's score is greater than other player's score,
        -1 if this player's score is less than other player's score, and 0 if
        they're equal.
        """
        # TODO
        if self.points > other.points:
            return 1
        elif self.points < other.points:
            return -1
        else:
            return 0

    def __str__(self):
        """
        Represent this player as a string

        returns: a string representation of this player
        """
        return 'Player %d\n\nScore: %.2f\n' % \
               (self.getIdNum(), self.getPoints())

#
# Problem 4: Representing a Computer Player
#

class ComputerPlayer(Player):
    """
    A computer player class.
    Does everything a Player does, but can also pick a word using the
    PickBestWord method.
    """
    def __init__(self, idNum, hand):
        Player.__init__(self, idNum, hand)

    def pickBestWord(self):
        """
        Pick the best word available to the computer player.

        returns: The best word (a string), given the computer player's hand and
        the wordlist
        """
        # TODO
        combination_dic = self.construt_combination_list(self.hand.copy())
        #print(combination_dic)
        try:
            best_word = max(combination_dic.items(), key=lambda x: x[1])[0]
        except:
            best_word = '.'
        #print('best word is', best_word)
        return best_word

    def is_valid_word(self, word, hand):
        """
        Returns True if word is in the word_list and is entirely
        composed of letters in the hand. Otherwise, returns False.
        Does not mutate hand or word_list.

        word: string
        hand: dictionary (string -> int)
        word_list: list of lowercase strings
        """
        # TO DO ...
        global words_points_dic
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

    def construt_combination_list(self, hand):
        """Part 1 is to transfer the hand(dic) to a hand_list which contains the letters
           Part 2 is to try all possible combination of word using all letters in hand_list and
                  store the results into a combination_list
           Part 3 is to reconstruct the words and select those correct ones and add their score
                  to the value of combination_dic
        """
        global words_points_dic
        hand_list = []
        combination_list = []
        combination_dic = {}
        for letter in hand.keys():  # hand is a dic; .keys return a list of the keys
            for j in range(hand[letter]):
                hand_list.append(letter)  # Part 1 finished
        # print(hand_list)
        list_of_tuple_combination = itertools.permutations(hand_list, len(hand_list))
        for tuple_combination in list_of_tuple_combination:
            combination_str = ''
            for k in range(0, len(tuple_combination)):
                combination_str = combination_str + tuple_combination[k]
            combination_list.append(combination_str)  # Part 2 finished
        # print(len(combination_list))
        for key in combination_list:
            for word_length in range(1, len(hand_list) + 1):
                status = self.is_valid_word(key[:word_length], hand.copy())
                # print(key[:word_length], status)
                if status:
                    combination_dic[key[:word_length]] = getWordScore(key[:word_length])
                    # Part 3 finished
        return combination_dic

    def playHand(self, callback, wordlist):
        """
        Play a hand completely by passing chosen words to the callback
        function.
        """
        while callback(self.pickBestWord(wordlist)):
            pass


class HumanPlayer(Player):
    """
    A Human player class.
    No methods are needed because everything is taken care of by the GUI.
    """

class Wordlist(object):
    """
    A word list.
    """
    def __init__(self):
        """
        Initializes a Wordlist object.

        postcondition: words are read in from a file (WORDLIST_FILENAME, a
        global constant) and stored as a list.
        """
        inputFile = open(r'/Users/fangzhou/PycharmProjects/problem_set4/words.txt')
        try:
            self.wordlist = []
            for line in inputFile:
                self.wordlist.append(line.strip().lower())
        finally:
            inputFile.close()
    def containsWord(self, word):
        """
        Test whether this wordlist includes word

        word: The word to check (a string)

        returns: True if word is in this Wordlist, False if word is not in
        Wordlist
        """
        return word in self.wordlist
    def getList(self):
        return self.wordlist

class EndHand(Exception): pass

class Game(object):
    """
    Stores the state needed to play a round of the word game.
    """
    def __init__(self, mode, wordlist):
        """
        Initializes a game.

        mode: Can be one of three constant values - HUMAN_SOLO, HUMAN_VS_COMP,
        and HUMAN_VS_HUMAN

        postcondition: Initializes the players nd their hands.
        """
        hand = Hand(HAND_SIZE)
        hand2 = Hand(HAND_SIZE, hand.handDict.copy())
        if mode == HUMAN_SOLO:
            self.players = [HumanPlayer(1, hand)]
        elif mode == HUMAN_VS_COMP:
            self.players = [HumanPlayer(1, hand),
                            ComputerPlayer(2, hand2)]
        elif mode == HUMAN_VS_HUMAN:
            self.players = [HumanPlayer(1, hand),
                            HumanPlayer(2, hand2)]
        self.playerIndex = 0
        self.wordlist = wordlist
    def getCurrentPlayer(self):
        """
        Gets the Player object corresponding to the active player.

        returns: The active Player object.
        """
        return self.players[self.playerIndex]
    def nextPlayer(self):
        """
        Changes the game state so that the next player is the active player.

        postcondition: playerIndex is incremented
        """
        if self.playerIndex + 1 < len(self.players):
            self.playerIndex = self.playerIndex + 1
            return True
        else:
            return False
    def gameOver(self):
        """
        Determines if the game is over

        returns: True if the playerIndex >= the number of players, False
        otherwise
        """
        return self.playerIndex >= len(self.players)
    def tryWord(self, word):
        if word == '.':
            raise EndHand()
        player = self.getCurrentPlayer()
        hand = player.getHand()
        if self.wordlist.containsWord(word) and hand.containsLetters(word):
            points = getWordScore(word)
            player.addPoints(points)
            hand.update(word)
            if hand.isEmpty():
                raise EndHand()
            return points
        else:
            return None
    def getWinner(self):
        return max(self.players)
    def getNumPlayers(self):
        return len(self.players)
    def isTie(self):
        return len(self.players) > 1 and \
               self.players[0].getPoints() == self.players[1].getPoints()
    def __str__(self):
        """
        Convert this game object to a string

        returns: the concatenation of the string representation of the players
        """
        string = ''
        for player in self.players:
            string = string + str(player)
        return string


wordlist = load_words()
get_words_to_points(wordlist)