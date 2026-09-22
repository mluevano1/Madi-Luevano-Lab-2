Import random

game_number = random randiant (1,10)
print (game_number)

guess=int(input ("Enter a number between 1 and 10"))

If guess>game_number:
    print ("lower")
elif guess<game_number:
    print ("higher!")
else:
    print ("Yay! You win")
