import numpy as np

def reduce(new_matrix):
    """Adds matrices together and gives the average"""
    global matrix
    try:
        result = np.array([[(matrix[i][j] + new_matrix[i][j]) / 2 for j in range(len(matrix[0]))] for i in range(len(matrix))]).reshape((28, 28))
        return result
    except NameError:
        return new_matrix
