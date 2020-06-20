# Write your code here
import random


def game():
    while True:
        w = input('> ')
        list_game = ['scissors', 'paper', 'rock']
        pc_choice = random.choice(list_game)
        if w == '!exit':
            print('Bye!')
            break
        elif w == '!rating':
            print(f'Your rating is: {rating[name]}')
        elif w == pc_choice:
            rating[name] += 50
            print(f'There is a draw ({pc_choice})')
        elif w == 'paper' and pc_choice == 'scissors':
            print(f'Sorry, but computer chose {pc_choice}')
        elif w == 'rock' and pc_choice == 'paper':
            print(f'Sorry, but computer chose {pc_choice}')
        elif w == 'scissors' and pc_choice == 'rock':
            print(f'Sorry, but computer chose {pc_choice}')
        elif w not in list_game:
            print('Invalid input')
        else:
            rating[name] += 100
            print(f'Well done. Computer chose {pc_choice} and failed')


def check_rating():
    rat = {}
    with open('rating.txt', 'r') as file:
        for line in file:
            r = (line.strip().split())
            rat[r[0]] = int(r[1])
    return rat


def define_win(i):
    list_game = option
    pc_choice = random.choice(list_game)
    ln_m = (len(option) - 1) // 2  # middle of list
    word_index = list_game.index(i)
    w1 = list_game[word_index + 1:word_index + ln_m + 1]
    win_list = []
    if len(w1) != 7:
        x = ln_m - len(w1)
        w2 = list_game[:x]
        win_list.extend(w2)
    win_list.extend(w1)

    if pc_choice == i:
        rating[name] += 50
        print(f'There is a draw ({pc_choice})')
    elif pc_choice in win_list:
        print(f'Sorry, but computer chose {pc_choice}')
    elif pc_choice not in win_list:
        rating[name] += 100
        print(f'Well done. Computer chose {pc_choice} and failed')


def game2():
    while True:
        w = input('> ')
        list_game = option
        if w == '!exit':
            print('Bye!')
            break
        elif w == '!rating':
            print(f'Your rating is: {rating[name]}')
        elif w in list_game:
            define_win(w)
        else:
            print('Invalid input')


name = input('Enter your name: ')
print(f'Hello, {name}')
rating = check_rating()
if name not in rating:
    rating[name] = 0

gm = input('> ')
if gm == '':
    print("Okay, let's start")
    game()
else:
    option = gm.split(',')
    print("Okay, let's start")
    game2()


