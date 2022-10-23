import sys
word_one, word_two = [x.lower() for x in sys.argv[1:] if x != " "]
print('True' if sorted(word_one) == sorted(word_two) else 'False')

