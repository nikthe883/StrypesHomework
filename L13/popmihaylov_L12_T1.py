import sqlite3
import sys

output = []
with open("retn5_dat.txt", "r+") as file:
    lines = file.readlines()
    for line in lines:
        line = line.split("^")
        thing = []
        for l in line:
            l = l.strip("~")
            thing.append(l)

        thing = [x for x in thing if x != "" and x != "\n"]
        if len(thing) < 5:
            print(thing)
        output.append(tuple(thing))
# print(output)

conn = sqlite3.connect('popmihaylov-food.db')
connection = conn.cursor()

connection.execute(""" CREATE TABLE IF NOT EXISTS food(
                code text,
                descript text,
                nmbr text,
                nutname text,
                retention text,
                UNIQUE(code, descript, nmbr, nutname, retention)
                )""")

conn.commit()

connection.executemany("INSERT INTO food VALUES (?,?,?,?,?)", output,)

query = sys.argv[1]


connection.execute(query)
print(connection.fetchone())

conn.close()
