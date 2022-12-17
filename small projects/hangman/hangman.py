import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def draw_hangman(guesses):
		if (guesses == 0):
				print("_________")
				print("|	 |")
				print("|")
				print("|")
				print("|")
				print("|")
				print("|________")
		elif (guesses == 1):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|")
				print("|")
				print("|")
				print("|________")
		elif (guesses == 2):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|	 |")
				print("|	 |")
				print("|")
				print("|________")
		elif (guesses == 3):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|	\|")
				print("|	 |")
				print("|")
				print("|________")
		elif (guesses == 4):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|	\|/")
				print("|	 |")
				print("|")
				print("|________")
		elif (guesses == 5):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|	\|/")
				print("|	 |")
				print("|	/ ")
				print("|________")
		elif (guesses == 6):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|	\|/")
				print("|	 |")
				print("|	/ \ ")
				print("|________")
				print("\n")


word = get_valid_word(words)
word_letters = set(word)
alphabet = set(string.ascii_uppercase)
used_letters = set()
guess_count = 0

while len(word_letters) > 0 and guess_count != 7:
    draw_hangman(guess_count)
    if guess_count == 6:
        print("YOU LOSE! :(")
        print("The word was %s." %word)
        break

    else:
        # print number of lives
        print('Number of LIVES: %s' % str(6-guess_count))

        # print letters used
        print('You have used these letters: %s' % ' '.join(used_letters))

        # print current word
        print('Current word: %s' % 
        ' '.join([letter if letter in used_letters else '-' for letter in word]))

        # get user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                guess_count += 1
        
        elif user_letter in used_letters:
            print('You have already entered this letter')

        else:
            print('Invalid character.')
        
        print("\n")

if len(word_letters) == 0:
    print("You guessed %s !" % word)

