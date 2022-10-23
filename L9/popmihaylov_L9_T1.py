from sys import argv

new_file = open(f'{argv[2]}', 'w')
with open(f"{argv[1]}", 'r') as file:
    for line in sorted(file):
        new_file.write(line)
new_file.close()
