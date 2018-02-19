print ('You have three (3) chances to enter your login.')
attempts = 0
while attempts < 3:
    YourName = input('Enter your login here: ')
    if YourName == 'Dylan':
        break
    print('login failed, try again')
    attempts = attempts + 1
if attempts < 3:
    print ('Successful login Dylan')
if attempts == 3:
    print ('Account locked')