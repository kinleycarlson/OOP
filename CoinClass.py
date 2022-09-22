import random

# The Coin class simulates a coin that can
# be flipped.

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):         ##always start class with this method and self paramter
        self.__sideup = 'Heads'   ##allows you to define all attributes of the object

# by putting '__' in front of sideup hides the attribute (has to do it everywhere)
    # when you hide the attribute, the program cannot affect the attributes
    
    ##this only has 1 attribute ('sideup')



    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.__sideup
