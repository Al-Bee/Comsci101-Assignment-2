import math
import random
round_num = 1
words = []
wins = 0
losses = 0
win_info = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

def main():
    global filename
    filename = input("Enter the name of the word file: ")
    play_game(filename)

def get_random_word(words):
    random_index = random.randrange(len(words))
    return words[random_index]

def play_game(filename):
    file = open(filename, 'r')
    global words
    words = file.read().split()
    file.close()
    print_greeting()
    print_rules()
    start_playing(words)

def print_greeting():
    name = input('Please enter your name: ')
    print(f"\nWelcome to Wordle 101 {name}\n")

def print_rules():
    print('========================================================================')
    print('                                 Rules')
    print('You have 6 guesses to figure out the solution.')
    print('All solutions are words that are 5 letters long.')
    print('Words may include repeated letters.')
    print('Letters that have been guessed correctly are displayed in uppercase.')
    print('Letters that are in the word but have been guessed in the wrong location')
    print('are displayed in lowercase.')
    print('========================================================================\n')

def start_playing(words):
    global round_num
    print(f'\nRound: {round_num}\n')
    word = get_random_word(words)
    play_round(word)
    play_again()

def play_round(word):
    count = 1
    result = ''
    while result != word.upper() and count < 7:
        print(f'Guess {count}:\n')
        player_guess = get_player_guess()
        result = check_guess(word, player_guess)
        print(' '.join(i for i in result) + '\n')
        check_win(result, word, count)
        count += 1

def get_player_guess():
    guess = input('Please enter your guess: ')
    while guess.isalpha() == False or len(guess) != 5:
        guess = input('Your guess must have 5 letters: ')
    return guess.lower()

def check_guess(word, guess):
    correct = {i: guess[i].upper() for i in range(0, 5) if guess[i] == word[i]}
    incorrect = {i: guess[i] for i in range(0, 5) if guess[i] != word[i]}
    remaining = [word[i] for i in range(0, 5) if guess[i] != word[i]]
    for i in incorrect:
        if incorrect[i] not in remaining:
            incorrect[i] = '_'
        else:
            remaining.pop(remaining.index(incorrect[i]))
    attempt = correct|incorrect
    attempt = dict(sorted(attempt.items()))
    result = ''.join([i for i in attempt.values()])
    return result

def check_win(result, word, count):
    if result == word.upper() and count < 7:
        print(f'Success! The word is {word}!\n')
        global wins
        wins += 1
        global win_info
        win_info[count] += 1
    elif count == 6:
        print(f'Better luck next time! The word is {word}!\n')
        global losses
        losses += 1

def play_again():
    choice = input("Please enter 'Y' to continue or 'N' to stop playing: ")
    while choice not in 'YN':
        print("Only enter 'Y' or 'N'!")
        choice = input("Please enter 'Y' to continue or 'N' to stop playing: ")
    if choice == 'Y':
        global round_num
        round_num += 1
        start_playing(words)
    else:
        print_info(win_info)
        return

def print_info(data_dict):
    global wins
    global round_num
    print()
    print('========================================================================')
    print('                                Summary')
    print(f'Win percentage: {math.ceil((wins/round_num) * 100)}%')
    print('Win Distribution:')
    for i in sorted(data_dict):
        print(f"{i}|{'#' * data_dict[i]}{data_dict[i]}")
    print('========================================================================')

main()
