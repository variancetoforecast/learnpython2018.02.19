import random

SecretNumber = random.randint(1,20)

print ('I am thinking of a number between 1 and 20')

count = 0

while True:
    YourGuess = input('Take a guess:')
    if int(YourGuess) == SecretNumber:
        break
    if int(YourGuess) > SecretNumber:
        print('Your Guess is too high')
    if int(YourGuess) < SecretNumber:
        print('Your Guess is too low')
    count = count + 1

print ('Congratulations you took' + str(int(count)) + ' guesses')