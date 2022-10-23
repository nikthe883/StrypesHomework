from sys import argv
input = '''11111111111111111111
10000000000000000001
10111111101011111101
10000000101010110101
10111111101010110101
10100000000010110101
10101110111110110101
10101010100000110101
10001000001000000001
11111111111111111111'''

lines = input.split('\n')
matrix = [[int(x) for x in line] for line in lines]
matrix[3][16] = 4


def printMaze(m):
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] == 1:
                m[row][col] = '#'
            elif m[row][col] == 0:
                m[row][col] = ' '
            elif m[row][col] == 4:
                m[row][col] = 'g'
    [print(' '.join(row)) for row in m]


def isValid(screen, x, y):
    if 0 <= x < len(screen) and 0 <= y < len(screen[0]) and screen[x][y] == 0 or screen[x][y] == 4 and screen[x][y] != "x":
        return True
    return False


# FloodFill function
def solveMaze(x, y):
    queue = [[x, y]]
    visited = []
    while queue:

        posX, posY = queue.pop()

        if matrix[posX][posY] == 4:
            printMaze(matrix)
            return

        matrix[posX][posY] = '.'
        visited.append([posX, posY])

        false = 0

        if isValid(matrix, posX + 1, posY):
            queue.append([posX + 1, posY])
        else:
            false += 1

        if isValid(matrix, posX - 1, posY):
            queue.append([posX - 1, posY])
        else:
            false += 1

        if isValid(matrix, posX, posY + 1):
            queue.append([posX, posY + 1])
        else:
            false += 1

        if isValid(matrix, posX, posY - 1):
            queue.append([posX, posY - 1])
        else:
            false += 1

        if false == 4:
            x, y = visited.pop()
            matrix[x][y] = "x"
            queue.append(visited.pop())


solveMaze(int(argv[1]), int(argv[2]))

