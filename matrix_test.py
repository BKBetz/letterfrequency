from letterfrequency.matrix import create_matrix
from letterfrequency.main import read_input
import numpy as np


def answer(test_str: str, en_matrix: np.array, du_matrix: np.array) -> dict:
    en_count = 0
    du_count = 0
    # convert string to matrix and convert that matrix to percentage matrix
    test_mat = create_matrix(test_str)
    test_sum = test_mat.sum()
    p_test_mat = np.array([(test_mat[x][y]/test_sum * 100) for x in range(len(test_mat)) for y in range(len(test_mat))]).reshape((28, 28))

    for x in range(len(p_test_mat)):
        for y in range(len(p_test_mat)):
            if p_test_mat[x][y] > 0:
                loss_en = en_matrix[x][y] - p_test_mat[x][y]
                loss_du = du_matrix[x][y] - p_test_mat[x][y]

                if loss_du < loss_en:
                    du_count += 1
                else:
                    en_count += 1

    total = du_count + en_count

    return {'dutch': du_count/total, 'english': en_count/total}


def test(file: str) -> []:

