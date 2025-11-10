import random as rand
number = rand.randint(1, 10)
COUNT = 0
guessed = False
print("Welcome to my game!")
while not guessed:
    guess = int(input("Guess any number between 1 and 10: "))
    COUNT += 1
    if guess == number:
        print("Congratulations, you guessed it right! you wonnnnn!!!!!!!!!!")
        guessed = True
    elif guess < number:
        print("Try a larger number you guessed.")
    else:
        print("Try a lower number you guessed.")
print(COUNT)
print("Game over!")