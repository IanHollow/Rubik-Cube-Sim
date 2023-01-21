import numpy as np
size = 2
rubik_cube = np.array([np.array([0]*4*size) for _ in range(3*size)])

# test visualize
for i in range(size, 2*size):
    for j in range(len(rubik_cube[i])):
        rubik_cube[i][j] = 1

for i in range(0, size):
    for j in range(2*size, 3*size):
        rubik_cube[i][j] = 1

for i in range(2*size, 3*size):
    for j in range(2*size, 3*size):
        rubik_cube[i][j] = 1


print(rubik_cube)
