import sys

arguments = sys.argv


def vigenere_cipher(text, key):
    '''Vigenere Cipher function. Takes a text and a key and returns the ciphered text'''

    cipher = ""
    index = 0
    character = "A"

    if text.islower():
        character = 'a'
    for char in text:
        if char.isalpha():

            offset = ord(key[index]) - ord(character)
            encrypted = chr((ord(char) - ord(character) + offset) % 26 + ord(character))
            cipher += encrypted
            index = (index + 1) % len(key)

        else:
            cipher += char

    return cipher


print(vigenere_cipher(*arguments[1:]))
