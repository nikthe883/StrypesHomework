import sys

arguments = sys.argv

if sorted(arguments[1:]) == arguments[1:]:
    print("sorted")
else:
    print("unsorted")
