
#IMPORT RANDOM FUNCTION

import random

#ASSIGN VARIABLES

computer = "Computer/Dealer"

player_bank = 0
computer_bank = 0
player_1_bank = 0
player_2_bank = 0

ace = 10
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10
jack = 10
queen = 10
king = 10

number_of_players = int(input("Number of Players: "))

if number_of_players > 2:

    print ("Maximum Number of Players is 2")

if number_of_players == 1:

    player_1 = input("Enter player 1 name: ")

else:

    player_1 = input("Enter player 1 name: ")
    player_2 = input("Enter player 2 name: ")
    




#MAKE LISTS FOR THE DECK

type_list = ["hearts", "clubs", "diamonds", "spades"]

type_length = len(type_list)

number_list = ["ace", "two", "three", "four", "five", "six" ,"seven", "eight", "nine", "ten", "jack", "queen", "king"]

number_length = len(number_list)


your_turn_1 = print (player_1,"'s turn")

choose_action = input ("hit or stand: ")

if choose_action == "hit":

    type_index = random.randint (0,type_length-1)

    number_name = random.randint (0,number_length-1)

    print ((number_list[number_name])+ " of " + (type_list[type_index]))


your_turn_2 = print (player_2,"'s turn")

choose_action = input ("hit or stand: ")

if choose_action == "hit":

    type_index = random.randint (0,type_length-1)

    number_name = random.randint (0,number_length-1)

    print ((number_list[number_name])+ " of " + (type_list[type_index]))


your_turn_3 = print (computer,"'s turn")

choose_action = input ("hit or stand: ")

if choose_action == "hit":

    type_index = random.randint (0,type_length-1)

    number_name = random.randint (0,number_length-1)

    print ((number_list[number_name])+ " of " + (type_list[type_index]))

if number_name == (ace, "ace of diamonds", "ace of clubs", "ace of spades"):

    player_bank += 10

if number_name == ("queen of hearts", "queen of diamonds", "queen of clubs", "queen of spades"):

    player_bank += 10

if number_name == ("king of hearts", "king of diamonds", "king of clubs", "queen of spades"):

    player_bank += 10

if number_name == (jack):

    player_bank += 10

if number_name == (two):

    player_bank += 2

if number_name == (three):

    player_bank += 3

if number_name == (four):

    player_bank += 4

if number_name == (five):

    player_bank += 5

if number_name == (six):

    player_bank += 6

if number_name == (seven):

    player_bank += 7

if number_name == (eight):

    player_bank += 8

if number_name == (nine):

    player_bank =+ 9

print (player_bank)
