import numpy as np

matrix = None
first_matrix = True


def onebyonereduce(all_matrices) -> np.array:
    for matrix in all_matrices:
        m = reduce(matrix)

    # convert the matrix values to percentages instead of ints
    total = m.sum()
    p_matrix = np.array([(m[x][y]/total * 100) for x in range(len(m)) for y in range(len(m))]).reshape((28, 28))
    return p_matrix


def reduce(new_matrix) -> np.array:
    """Adds matrices together and gives the average"""
    global matrix, first_matrix

    if first_matrix == True:
        matrix = new_matrix
        first_matrix = False

    else:
        matrix = np.array([[(matrix[i][j] + new_matrix[i][j]) for j in range(len(matrix[0]))] for i in
                           range(len(matrix))]).reshape((28, 28))

    return matrix
