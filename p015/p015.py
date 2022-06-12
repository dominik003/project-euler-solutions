import numpy as np

grid_size = (20, 20)

possibility_matrix = np.zeros((grid_size[0] + 1, grid_size[1] + 1), dtype=np.longlong)

possibility_matrix[0:possibility_matrix.shape[0]+1, 0] = 1
possibility_matrix[0, 0:possibility_matrix.shape[1]+1] = 1

# Pascal's triangle calculation
for row in range(1, possibility_matrix.shape[0]):
    for col in range(1, possibility_matrix.shape[1]):
        possibility_matrix[row, col] = possibility_matrix[row - 1, col] + possibility_matrix[row, col - 1]

print(possibility_matrix[grid_size])
