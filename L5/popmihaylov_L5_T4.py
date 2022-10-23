from sys import argv


def palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])


print(palindrome(argv[1]))
