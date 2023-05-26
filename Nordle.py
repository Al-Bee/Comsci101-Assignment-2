import math

def main():
    global filename
    filename = input("Enter the name of the word file: ")
    play_game(filename)

def play_game(filename):
    file = open(filename, 'r')
    words = file.read().split()
    file.close()
    round_num = 1
    wins = 0
    win_info = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    print_greeting()
    print_rules()
    start_playing(words, round_num, wins, win_info)

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

def start_playing(words, round_num, wins, win_info):
    print(f'\nRound: {round_num}\n')
    word = get_random_word(words)
    wins, win_info = play_round(word, wins, win_info)
    play_again(words, round_num, wins, win_info)

def play_round(word, wins, win_info):
    count = 1
    result = ''
    while result != word.upper() and count < 7:
        print(f'Guess {count}:\n')
        player_guess = get_player_guess()
        result = check_guess(word, player_guess)
        print(' '.join(i for i in result) + '\n')
        wins, win_info = check_win(result, word, count, wins, win_info)
        count += 1
    return wins, win_info

def get_player_guess():
    guess = input('Please enter your guess: ')
    while guess.isalpha() == False or len(guess) != 5:
        guess = input('Your guess must have 5 letters: ')
    return guess.lower()

def check_guess(word, guess):
    correct = [[i, guess[i].upper()] for i in range(0, 5) if guess[i] == word[i]]
    incorrect = [[i, guess[i]] for i in range(0, 5) if guess[i] != word[i]]
    remaining = [word[i] for i in range(0, 5) if guess[i] != word[i]]
    for i in incorrect:
        if i[1] not in remaining:
            i[1] = '_'
        else:
            remaining.pop(remaining.index(i[1]))
    return ''.join([i[1] for i in sorted(correct + incorrect)])

def check_win(result, word, count, wins, win_info):
    if result == word.upper() and count < 7:
        print(f'Success! The word is {word}!\n')
        wins += 1
        win_info[count] += 1
        return wins, win_info
    elif count == 6:
        print(f'Better luck next time! The word is {word}!\n')
        return wins, win_info
    else:
        return wins, win_info

def play_again(words, round_num, wins, win_info):
    choice = input("Please enter 'Y' to continue or 'N' to stop playing: ")
    while choice not in 'YN':
        print("Only enter 'Y' or 'N'!")
        choice = input("Please enter 'Y' to continue or 'N' to stop playing: ")
    if choice == 'Y':
        round_num += 1
        start_playing(words, round_num, wins, win_info)
    else:
        print_info(round_num, wins, win_info)
        return

def print_info(round_num, wins, win_info):
    print('\n========================================================================')
    print('                                Summary')
    print(f'Win percentage: {math.ceil((wins/round_num) * 100)}%\nWin Distribution:')
    for i in sorted(win_info):
        print(f"{i}|{'#' * win_info[i]}{win_info[i]}")
    print('========================================================================')
