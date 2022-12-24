import pickle
import random
import sqlite3
import time
def crypto():
        # lettersWithOutSplit = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        # numbersWithOutSplit = "1 2 3 4 5 6 7 8 9 0"
        # letters = lettersWithOutSplit.split(" ")
        # numbers = numbersWithOutSplit.split(" ")
        rand = random.randint(1, 20)
        if rand == 1: 
            hashed = "BAG LOST"
        else:
            age = random.randint()
            hashed = "Age:" + str(random.randint(18, 117)) + "Height: " + str(random.randint(2, 84))
        with open("output.txt", "a") as f:
            f.append(hashed) 