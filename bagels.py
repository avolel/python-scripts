import random

NUM_DIGITS = 3 #Number of digits to guess
MAX_GUESSES = 10 #Max Number of Guesses

def Main():
    number_of_guesses = 1
    guess = ''
    clues = []
    print('''Bagels, a deductive  logic Game. 
          
          I am thinking of a {} digit number with no repeated digits.
          Try to guess what it is. Here are some clues:
          
          Pico = One digit is correct but in the wrong position.
          Fermi = One digit is correct and in the right position.
          Bagels = No digit is correct.

          For example:
          If the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
          '''.format(NUM_DIGITS))
    
    print("I am thinking of a number.")
    print("You have {} guesses to guess the number.".format(MAX_GUESSES))
    secret_number = getSecretNumber()

    while True: #MAIN Loop
        while number_of_guesses <= MAX_GUESSES:
            print("Guess #{}: ".format(number_of_guesses))
            guess = input("> ")

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guesses must be {} digits long. Gusses must be a number.".format(NUM_DIGITS))
                print("Guess #{}: ".format(number_of_guesses))
                guess = input("> ")
        
            if guess == secret_number:
                print("Congratulations! You guessed the secret number. The secret number is {}".format(secret_number))
                print("Thanks for playing!")
                print("Do you want to play again? (yes or no)")
                if not input(">").lower().startswith('y'):
                   print("Goodbye!")
                   exit(0)
                else:
                    number_of_guesses = 1
                    secret_number = getSecretNumber()
                    print("I am thinking of a number.")
                    print("You have {} guesses to guess the number.".format(MAX_GUESSES))
            else:
                number_of_guesses += 1
                clues.clear()
                for i in range(len(guess)):
                    if guess[i] == secret_number[i]:
                        #a correct digit is in the correct place
                        clues.append("Fermi: {} is in the correct postion".format(guess[i]))
                    elif guess[i] in secret_number:
                        #a correct digit is in the wrong place
                        clues.append("Pico: {} is the correct digit but it's in the wrong position".format(guess[i]))
        
            if len(clues) == 0:
                print("Bagels")
            else:
                clues.sort()
                print(' , '.join(clues))                
        
            if number_of_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The secret number was {} ".format(secret_number))
                print("Do you want to play again? (yes or no)")
                if not input(">").lower().startswith('y'):
                    print("Goodbye!")
                    exit(0)
                else:
                    number_of_guesses = 1
                    secret_number = getSecretNumber()
                    print("I am thinking of a number.")
                    print("You have {} guesses to guess the number.".format(MAX_GUESSES))

def getSecretNumber():
    numbers = list('0123456789') #list of digits 0 to 9
    random.shuffle(numbers) #shuffle the numbers into random order

    #Get the first NUM_DIGITS in the list for secret number:
    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number

if __name__ == "__main__":
    Main()