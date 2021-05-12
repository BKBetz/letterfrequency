import numpy as np

def reduce(new_matrix):
    global matrix
    try:
        print(matrix, new_matrix)
        result = [[(matrix[i][j] + new_matrix[i][j]) / 2 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        return result
    except NameError:
        return new_matrix


m = np.matrix([[1, 2], [3, 4]])
print(m)
# matrix = reduce(m)





# print('na 1 keer',matrix)
# ma = np.matrix([[5, 4], [3, 2]])
# matrix = reduce(ma)
# print('na 2 keer', matrix)