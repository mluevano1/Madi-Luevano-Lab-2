import random

game_number = random.randint (1,10)
guesses = []

while (True):
    guess=int(input ("Enter a number between 1 and 10"))
    guesses.append(guess)

    if guess>game_number:
        feedback = "lower"
    elif guess<game_number:
        feedback = "higher!"
    else:
        print ("You win!")
        print (f"You got it in {len(guesses)} guesses.")
        print ("Guess history:")
        for number, recorded_guess in enumerate(guesses, start=1):
            if recorded_guess > game_number:
                recorded_feedback = "lower"
            elif recorded_guess < game_number:
                recorded_feedback = "higher"
            else:
                recorded_feedback = "correct"
            print (f"{number}. {recorded_guess} ({recorded_feedback})")
        break

    print (feedback)
