import random
    
def guessing():
    right_number = random.randint(1, 10)
    guess = input('Guess a number from 1 to 10 >> ')
    intguess = int(guess)
    while True:
        if intguess == right_number:
            print('Yup you got it!')
            break
        elif intguess > right_number:
            print('Try a bit lower')
            guess = input('Guess a number from 1 to 10 >> ')
            intguess = int(guess)
        elif intguess < right_number:
            print('Try a bit higher')
            guess = input('Guess a number from 1 to 10 >> ')
            intguess = int(guess)


guessing()