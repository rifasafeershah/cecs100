
import random

#assign variables

player_name = input("Enter player name: ")

computer = "Computer"

player = player_name

#set turns

your_turn_1 = print (player,"'s turn")

number = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))

while number > 3 or number < 1:

    print ("Your Choice is Invalid")

    number = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))
    
if number == 1:

    player_choice_1 = "rock"

    print (player, "chose:", player_choice_1)

if number == 2:

    player_choice_1 = "paper"

    print (player, "chose:", player_choice_1)

if number == 3:

    player_choice_1 = "scissors"

    print (player, "chose:", player_choice_1)

#set turns

your_turn_2 = print (computer,"'s turn")

number = random.randint (1, 4)

if number > 3:

    print ("Invalid Choice")
    
if number == 1:

    player_choice_2 = "rock"

    print ( computer, "chose:", player_choice_2)

if number == 2:

    player_choice_2 = "paper"

    print ( computer, "chose:", player_choice_2)

if number == 3:

    player_choice_2 = "scissors"

    print ( computer, "chose:", player_choice_2)
    
#CONDITIONS OF WIN

if player_choice_1 == rock and player_choice_2 == paper:

    print (computer, "wins the game!" )

elif player_choice_1 == paper and player_choice_2 == scissors:

    print (computer, "wins the game" )

elif player_choice_1 == scissors and player_choice_2 == 1:

    print (computer, "wins the game" )

elif player_choice_1 == 2 and player_choice_2 == 1:

    print (player, "wins the game" )

elif player_choice_1 == 3 and player_choice_2 == 2:

    print (player, "wins the game" )

elif player_choice_1 == 1 and player_choice_2 == 3:

    print (player, "wins the game" )
