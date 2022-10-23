import sys
arguments = sys.argv


def caesar_cipher(text, key):
    """Function that returns Caesar cipher.
    First input is the text, second input is the shift"""

    result = ""

    for i in text:
        if i.isalpha():
            if i.isupper():
                result += chr((ord(i) + int(key) - 65) % 26 + 65)

            else:
                result += chr((ord(i) + int(key) - 97) % 26 + 97)
        else:
            result += i

    return result


print(caesar_cipher(*arguments[1:]))
