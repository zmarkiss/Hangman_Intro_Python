#  write your code here
from random import choice
from string import ascii_lowercase


def hangman():
    word_bank = ['python', 'java', 'swift', 'javascript']
    word_choice = choice(word_bank)
    word = ['-' for n in range(len(word_choice))]
    letter_catcher = []
    guess = 1

    while guess <= 8:

        d = [i for i in word if i != '-']
        if len(word_choice) == len(d):
            print(F'\nYou guessed the word {"".join(word)}!\nYou survived!')
            return 1

        print(f'\n{"".join(word)}')
        le = input(f'Input a letter:')

        if len(le) != 1:
            print('Please, input a single letter.')
            continue

        if le not in ascii_lowercase:
            print('Please, enter a lowercase letter from the English alphabet.')
            continue

        if le in letter_catcher:
            print("You've already guessed this letter.")
            continue
        letter_catcher.append(le)

        for i in range(len(word_choice)):
            if word[i] != le:
                if le == word_choice[i]:
                    word[i] = le
            else:
                print('No improvements.')
                guess += 1
                print(guess)
                break

        if le not in word_choice:
            print("That letter doesn't appear in the word.")
            guess += 1
        if guess == 9:
            print('You lost!')
            return guess


print('H A N G M A N')
win_score = list()
lose_score = list()
counter = str()
while counter != 'exit':
    counter = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if counter == 'results':
        print(f'You won: {win_score.count(1)} times.')
        print(f'You lost: {win_score.count(9)} times.')
        continue
    if counter == 'play':
        win_score.append(hangman())

quit()
