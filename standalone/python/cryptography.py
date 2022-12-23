import pickle
import random
import sqlite3
import time
class crypto:
    def __init__(self):
        lettersWithOutSplit = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        numbersWithOutSplit = "1 2 3 4 5 6 7 8 9 0"
        letters = lettersWithOutSplit.split(" ")
        numbers = numbersWithOutSplit.split(" ")
        self.hashed = ""
        for x in range(5):
            charnum = random.randint(1, 2)
            if charnum == 1:
                lettchoice = random.sample(letters, k=1)
                print(lettchoice)
                input("")