import random


def init():
    global low, high, secret_num, count, limit, yesses, nos
    low = 1
    high = 100
    secret_num = random.randint(low, high)
    count = 0
    limit = 7
    yesses = ['Y', 'YES', 'YEAH', 'SURE', 'OK', 'OKAY', 'MHM', 'MHMM', 'YUP', 'YEP']
    nos = ['N', 'NO', 'NAH', 'UH UH', 'PASS', 'NO WAY', 'NO THANKS']
    welcome = f'''
This is a number guessing game by Cameron De Robertis.

You've got {limit} guesses to find a secret number between {low} and {high}.
Don't worry, I'll help you along the way!
'''
    print(welcome)


def game():
    global count
    while count < limit:
        def prompt_guess():
            global guess
            guess = input(f'Guess a number between {low} and {high}: ')
            if not guess.isnumeric():
                print('Pick an actual number!')
                prompt_guess()
            elif int(guess) > high or int(guess) < low:
                print('Number out of range. Pick another!')
                prompt_guess()
            guess = int(guess)

        prompt_guess()
        count += 1
        if guess == secret_num:
            print('Correct!')
            break
        elif count < limit:
            if guess < secret_num:
                print('Higher!')
            else:
                print('Lower!')
        else:
            print(f'Game over. The secret number was {secret_num}.')
            print()


def replay_prompt():
    replay = input('Play again?: ').upper()
    if replay in yesses:
        init()
        game()
        replay_prompt()
    elif replay in nos:
        return
    else:
        print('Please indicate yes or no.')
        replay_prompt()


init()
game()
replay_prompt()

print('''
Thanks for playing, if you had fun, follow my other projects:
@cmderobertis
www.cmderobertis.net
''')
