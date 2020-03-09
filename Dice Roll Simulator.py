import random
def one_die():
        print('You have rolled ', random.randint(1, 6))


def two_die():
    die_one = random.randint(1, 6)
    die_two = random.randint(1, 6)
    print(f'You have rolled {die_one}, {die_two}')


play_now = False
while True:
    query = input('Do you want to play using 1 die or two dice? Reply with 1 or 2: ')
    
    if query == '1':
        one_die()

    elif query == '2':
        two_die()

    else:
        print('Please read the instructions very carefully!!!')


    plays = {"yes", "y", "start", "begin"}
    start_play = input('Do you want to play again? ').lower()
    
    if start_play in plays:
        play_now = True
        print('Okay carry on.')

    else:
        print('Goodbye')
        play_now = False
        exit()




