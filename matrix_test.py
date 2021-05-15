from letterfrequency.matrix import create_matrix
import numpy as np


def read_input(file: str) -> list:
    """Read the given file and seperate per line"""
    with open(file, encoding='utf-8') as f:
        # we use .read().splitlines() instead of .readlines() to remove "\n" in an easy way
        data = f.read().splitlines()
    return data


def answer(test_str: str, en_matrix: np.array, du_matrix: np.array) -> dict:
    total_loss_en = 0
    total_loss_du = 0
    # convert string to matrix and convert that matrix to percentage matrix
    test_mat = create_matrix(test_str)
    test_sum = test_mat.sum()
    p_test_mat = np.array([(test_mat[x][y]/test_sum * 100) for x in range(len(test_mat)) for y in range(len(test_mat))]).reshape((28, 28))

    for x in range(len(p_test_mat)):
        for y in range(len(p_test_mat)):
            if p_test_mat[x][y] > 0:
                loss_en = en_matrix[x][y] - p_test_mat[x][y]
                loss_du = du_matrix[x][y] - p_test_mat[x][y]
                total_loss_du += loss_du
                total_loss_en += loss_en

    totalloss = total_loss_en + total_loss_du

    return {'dutch': total_loss_du/totalloss, 'english': total_loss_en/totalloss}


def test(data: str, en_matrix: np.array, du_matrix: np.array) -> dict:
    # if data is just one sentence we will return it once
    try:
        results = {'dutch': 0, 'english': 0}
        sentences = read_input(data)
        for sentence in sentences:
            print('sentence', sentence)
            result = answer(sentence, en_matrix, du_matrix)
            print('result', result)
            outcome = max(result, key=lambda key: result[key])
            print('outcome', outcome)

            results[outcome] += 1

        return results

    except FileNotFoundError:
        # data is a string so we only return the answer function to show the percentage of english or dutch
        return answer(data, en_matrix, du_matrix)

