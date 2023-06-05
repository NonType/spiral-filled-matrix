# create a matrix
size = int(input())
matrix = [list([0] * size) for i in range(size)]
# convert the first row of the matrix into numbers from 1 to size
num = 1  # the number of matrix filler
for i in range(size):
    matrix[0][i] = num
    num += 1

x = size - 1
y = 0
r = size
while num <= size * size:  # until the filler is less than and equal to the number of matrix numbers
    r -= 1
    for _ in range(r):  # vertical cycle
        y += 1
        matrix[y][x] = num
        num += 1

    for _ in range(r):  # horizontal cycle
        x -= 1
        matrix[y][x] = num
        num += 1
    r -= 1
    for _ in range(r):  # vertical cycle
        y -= 1
        matrix[y][x] = num
        num += 1
    for _ in range(r):  # horizontal cycle
        x += 1
        matrix[y][x] = num
        num += 1
for i in matrix:
    print(*i)
