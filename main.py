# Python Day - 8 -- Ceasar Cipher
# 11/05/2023
# Functions with inputs, arguments vs parameters, loops, conditions, validation.
# ------------------------------------------------------------------------------------

from replit import clear
from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# method for the cipher
def cipher(ciphered_text, shift_amount, cipher_direction):
    # container to store the encoded or the decoded cipher
    cipher_text = ''

    if cipher_direction == 'decode':
        shift_amount *= -1

    # Looping through the user message
    for char in ciphered_text:
        # condition to not change non-letter char
        if char not in alphabet:
            cipher_text += char
        else:
            # Getting the position of the letters in the user message
            position = (alphabet.index(char) + shift_amount) % 26 
            # % 26 to avoid out of range issue

            cipher_text += alphabet[position]
    # Print the result
    print(
        f"\nYour {cipher_direction}d result is: '{cipher_text}'\n"
    )

# Run the app again condition
is_finished = False
while not is_finished:
    
    # display the logo
    print(logo + '\n')
    
    # Condition to make sure the direction input is 'encode' or 'decode'.
    while True:
        direction = input("Type 'encode' to encrypt, or 'decode' to decrypt, type 'e' to exit.:\n").lower()
        if direction == 'encode' or direction == 'decode':
            break
        else:
            print("Invild! Please enter 'encode' or 'decode'.")

    # Getting the user message
    text = input("Type your message:\n").lower()

    # Condition to make sure the shift is a whole number.
    while True:
        shift = input("Type the shift number:\n")
        if shift.isdigit():
            shift = int(shift)
            break
        else:
            print("Invild! Please enter a whole number as a key.")

    
    # Calling the cipher method
    cipher(text, shift, direction)

    while True:
        again = input("Would you like to run the cipher again? Type 'Y' or 'N'\n").lower()
        if again == 'y' or again == 'n':
            break
        else:
            print("Invild! Please Type 'Y' or 'N'.\n")

    if again == 'y':
        clear()
    else:
        print("Goodbye!")
        is_finished = True