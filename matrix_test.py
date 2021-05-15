from letterfrequency.matrix import create_matrix
import numpy as np

du = create_matrix('../data/bzt.txt')
en = create_matrix('../data/alice.txt')


def read_input(file: str) -> list:
    """Read the given file and seperate per line"""
    with open(file, encoding='utf-8') as f:
        # we use .read().splitlines() instead of .readlines() to remove "\n" in an easy way
        data = f.read().splitlines()
    return data


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


def test(data: str, en_matrix: np.array, du_matrix: np.array) -> dict:
    # if data is just one sentence we will return it once
    try:
        results = {'dutch': 0, 'english': 0}
        sentences = read_input(data)
        for sentence in sentences:
            result = answer(sentence, en_matrix, du_matrix)
            print(result)

    except FileNotFoundError:
        # data is a string so we only return the answer function to show the percentage of english or dutch
        return answer(data, en_matrix, du_matrix)


test('../data/sentences.nl-en.txt', en, du)
