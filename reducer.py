import numpy as np

matrix = None
first_matrix = True

def onebyonereduce(all_matrices):
    for matrix in all_matrices:
        m = reduce(matrix)
    return m

def reduce(new_matrix):
    """Adds matrices together and gives the average"""
    global matrix, first_matrix

    if first_matrix == True:
        matrix = new_matrix
        first_matrix = False

    else:
        matrix = np.array([[(matrix[i][j] + new_matrix[i][j]) for j in range(len(matrix[0]))] for i in
                           range(len(matrix))]).reshape((28, 28))

    return matrix