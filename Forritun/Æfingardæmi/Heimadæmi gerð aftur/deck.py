import random

In a deck, there are four
suits -- hearts, spades, diamonds, and clubs --, that we represent by their first
letters: H(h), S(s), D(d), C(c)


Ace, 2-10,
Jack, Queen, and King –
with ranks 1-13 in that order

a deck has 52
cards. A playing hand has thirteen cards.

class PlayingHand():
    def __init__(self):
        # A constant, NUMBER_CARDS, with value 13.
        # The constructor creates
        # a hand of 13 blank cards.

    def add_card():
        # with the parameter denoting a card. The
        # methods adds the given card to the playing hand at the first
        # blank position.

    def __str__():
        # for returning a string representation of a
        # playing hand, consisting of a single line containing a string
        # representation of each card.

class Card():
    def __init__(self, rank, suit):


    def is_blank(self):
        # returns True if a card is blank, otherwise False

    def __str__(self):
# right justified field
# of 3 characters: the ranks followed by the suit. 
# If a card has
# default values, then 'blk' (blank)

class deck():
    def __init__(self):
        self.all_cards=[]
        for number in range(13):
            for letter in 'SHDC':
                if number==1:
                    all_cards.append('A'+letter)
                elif number==11:
                    all_cards.append('J'+letter)
                elif number==12:
                    all_cards.append('Q'+letter)
                elif number==13:
                    all_cards.append('K'+letter)
                else:
                    all_cards.append(str(number)+letter)

    def __str__(self):
        for i in range(4):
            print (" ".join(all_cards[i*13:(i+1)*13]) + "\n")
        # for returning a string representation of a
        # deck, consisting of 4 lines containing 13 cards each.

    def shuffle(self):
        self.all_cards.shuffle()
        # Shuffles the cards in the deck.
    
    def deal(self):
        single_card=self.all_cards.pop()
        return single_cards

