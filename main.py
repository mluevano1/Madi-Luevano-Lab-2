import random

game_number = random.randint (1,10)
while (True):

    print (game_number)

    guess=int(input ("Enter a number between 1 and 10"))


    if guess>game_number:
     print ("lower")
    elif guess<game_number:
        print ("higher!")
    else:
        print ("You win!")
