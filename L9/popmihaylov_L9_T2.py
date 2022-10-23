from sys import argv
my_dict = {}
with open(f"{argv[1]}", "r") as file:
    for line in file.readlines():
        key, value = line.strip().split(":")
        if key not in my_dict:
            my_dict[key] = []
        my_dict[key].append(value)

print(*my_dict[argv[2]])
