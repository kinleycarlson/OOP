import random

class Insect:
    
    def __init__(self,l,w): #allows the user to input values
        self.__wings = w
        self.__legs = l
        self.__flight = 0

    def flight_length(self):
        self.__flight = random.randint(1,10)

    def get_flight(self):
        return self.__flight
