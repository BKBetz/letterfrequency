import numpy as np

# matrix filled with zero's
matrix = np.zeros((28, 28))

def onebyonereduce(all_matrices) -> np.array:
    """Gives reduce() a single matrix as input and converts the matrix to percentages"""
    # runs reduce() with every matrix
    for matrix in all_matrices:
        m = reduce(matrix)

    # convert the matrix values to percentages instead of ints
    total = m.sum()
    p_matrix = np.array([(m[x][y]/total * 100) for x in range(len(m)) for y in range(len(m))]).reshape((28, 28))
    return p_matrix


def reduce(new_matrix) -> np.array:
    """Adds matrices together"""
    global matrix

    # adds two matrices together
    matrix = np.array([[(matrix[i][j] + new_matrix[i][j]) for j in range(len(matrix[0]))] for i in
                       range(len(matrix))]).reshape((28, 28))

    return matrix
