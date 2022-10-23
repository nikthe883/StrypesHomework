import sys

arguments = sys.argv
my_dict = {}

for t in arguments[1]:
    if t not in my_dict:
        my_dict.setdefault(t, 0)
    my_dict[t] += 1


print(list(my_dict.items()))
