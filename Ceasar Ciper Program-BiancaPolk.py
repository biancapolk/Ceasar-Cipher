# Ceasar cipher Progrom
# Using a for loop
# by Bianca Polk
from pip._vendor.distlib.compat import raw_input

key = 3
plaintextFile = open("plaintext.txt", "r")

ciphertextFile = open("ciphertext.txt", "r")
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def encrypt(plaintextFile, key):
    result = ""

    if plaintextFile.mode == 'r':
        plaintext = plaintextFile.read()

        # transverse the plain text
    for letter in plaintext:
        if letter in SYMBOLS:  # if the letter is actually a letter
            # find the corresponding ciphertext letter in the alphabet
            letter_index = (SYMBOLS.find(letter) + key) % MAX_KEY_SIZE

            result = result + SYMBOLS[letter_index]
        else:
            result = result + letter

        # printing the above function results to ciphertext.txt
        file = open("ciphertext.txt", "w")
        file.write(result)
        file.close()
    #printing result to console
    print(result)



def decrypt(ciphertext, key):
        result = ""
        if ciphertextFile.mode == 'r':
            ciphertext = ciphertextFile.read()

        for letter in ciphertext:
            if letter in SYMBOLS:  # if the letter is actually a letter
                # find the corresponding ciphertext letter in the alphabet
                letter_index = (SYMBOLS.find(letter) - key) % MAX_KEY_SIZE

                result = result + SYMBOLS[letter_index]
            else:
                result = result + letter

            # printing the above function results to ciphertext.txt
            file = open("plaintext.txt", "w")
            file.write(result)
            file.close()
        # printing result to console
        print(result)



# Break
def breakProgram():
    # loop through every possible key

    incomplete = True

    while incomplete:

        for i in range(MAX_KEY_SIZE):

            # It is important to set translated to the blank string so that the
            # previous iteration's value for translated is cleared.
            translated = ''

            for symbol in ciphertextFile:

                  if symbol in SYMBOLS:

                     num = SYMBOLS.find(symbol)
                     num = num - i

                     if num < 0:
                        num = num + MAX_KEY_SIZE

                     translated = translated + SYMBOLS[num]

                  else:
                     translated = translated + symbol

            print('Hacking key #%s: %s   ' % (i, translated))

            print("Is text correct? (y or n)")
            verify = input()
            if verify.lower() not in ('y', 'n'):
                print("Not appropriate choice - please enter y or n")
            if verify == 'n':
                continue
            if verify == 'y':
                print("Key is Correct!!")
                return
            else:
                break


def menu():
    menu = {}

    menu['1'] = "Encript"
    menu['2'] = "Decript"
    menu['3'] = "Break"
    menu['4'] = "Exit"

    while True:
        options = menu.keys()
        print("--------------------CRYPTIC MENU OPTIONS: --------------------")

        for entry in options:
            print(entry, menu[entry])

        selection = raw_input("Please select a menu option:")
        if selection == '1':
            encrypt(plaintextFile, key)
        elif selection == '2':
            decrypt(ciphertextFile, key)
        elif selection == '3':
            breakProgram()
            #continue
        elif selection == '4':
            print("End of Program")
            break
        else:
            print
            "Unknown Option Selected!"


menu()
