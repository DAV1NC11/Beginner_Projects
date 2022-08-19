import random
actual_value = random.randrange(1, 20)
actual_value = int(actual_value)
name = input('What is your name?')
print(f'Well {name},I am thinking of a number between 1 and 20, what is the number?')
guess = int(input('>'))
game = True
while game:
    if (float(guess)>int(actual_value)):
        print('The value you are looking for is lower than this!')
        guess = int(input('> '))
        game = True

    elif guess not in range(1, 21, 1):
        print('Please read the instructions very carefully')
        guess = int(input('> '))
        game = True

    elif (float(guess)<float(actual_value)):
        print('The value you are looking for is higher than this!')
        guess = int(input('> '))
        game = True
        

    else:
        print('You guessed the right number!')
        game = False
        quit()
