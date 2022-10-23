import sys
arguments = sys.argv

more_than_one = False

for i in arguments[1:]:
    if arguments.count(i) > 1:
        more_than_one = True
        break

print(more_than_one)
