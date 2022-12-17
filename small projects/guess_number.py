import random

def guess_person_against_computer(upper_bound):
    random_number = random.randint(1, upper_bound)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and %s: " %upper_bound))
        if guess < random_number:
            print("Too low.")
        elif guess > random_number:
            print("Too high.")
    print("Congrats. You gueesed the number!")

def guess_computer_against_person(upper_bound):
    lower_bound = 1
    feedback = ''
    while feedback != 'c':
        guess = random.randint(lower_bound, upper_bound)
        feedback = input("""
        Is %s too high (H), too low (L), or correct (C)??\n""" % feedback).lower()

        if feedback == 'h':
            upper_bound = guess - 1

        elif feedback == 'l':
            lower_bound = guess + 1

    print("Computer guessed your number!")

if __name__ == "__main__":
    option = input("""
    (1) for person guesses against to computer number
    (2) for computers guesses against your number\n""")
    upper_bound = input("Enter upper bound of numbers: ")

    if option == "1": guess_person_against_computer(int(upper_bound))
    elif option == "2": guess_computer_against_person(int(upper_bound))
