import numpy as np
import itertools as it
import pandas as pd


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
          "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
          "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
          "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
          "X": 8, "Z": 10}

def wrong_length(letter):
    if len(letter)>1:
        print "You can only enter one letter at a time! Try again."
        letter=raw_input("Enter 1 of the letters you have in lower case: ")
    elif (letter) is '':
        print "You forgot to enter a letter! Try again."
        letter=raw_input("Enter 1 of the letters you have in lower case: ")
    
    
l1=raw_input("Enter 1 of the letters you have in lower case: ")
wrong_length(l1)
l2=raw_input("Enter 1 of the letters you have in lower case: ")
wrong_length(l2)
l3=raw_input("Enter 1 of the letters you have in lower case: ")
wrong_length(l3)
l4=raw_input("Enter 1 of the letters you have in lower case: ")
wrong_length(l4)
l5=raw_input("Enter 1 of the letters you have in lower case: ")
wrong_length(l5)
l6=raw_input("Enter 1 of the letters you have in lower case: ")
wrong_length(l6)
l7=raw_input("Enter 1 of the letters you have in lower case: ")
wrong_length(l7)

board=raw_input("Enter the letter you want to use from the board: ")

avail=[l1,l2,l3,l4,l5,l6,l7,board] #list of letters you have
dictionary=np.loadtxt('words.txt',dtype='str') #library of words you can use in scrabble
words = set(word.strip().lower() for word in dictionary) #strip the words in dictionary to read individual letters


for i in range(3,8): #words of length 3 to 8
    
    perms = set(''.join(letters) for letters in it.permutations(avail,i)) #all the permutations of the letters you have
    res = [word for word in perms if word in words] #all the permutations which match words in the dictionary

    res1=[word for word in res if board in word]
    word_scores=[]
    for j in res1:
        def score_calc(word):
            x=0
            for k in range (len(word)):
                x+=scores[word[k].upper()]
            return x
        word_scores.append(score_calc(j))

    d = {'Word':res1,'Score':word_scores}
    answer= pd.DataFrame(d) #create data frame of words and scores
    answer=answer.sort_values(by=['Score'],ascending=False) #sorts according to score
    if not answer.empty:
        answer=answer.to_string(index=False)
        print ('\n %s Letter Words:' %(i))
        print ('')
        print answer
