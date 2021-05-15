from matrix import create_matrix
import numpy as np


def read_input(file: str) -> list:
    """Read the given file and seperate per line"""
    with open(file, encoding='utf-8') as f:
        # we use .read().splitlines() instead of .readlines() to remove "\n" in an easy way
        data = f.read().splitlines()
    return data


def answer(test_str: str, en_matrix: np.array, du_matrix: np.array) -> dict:
    count_en = 0
    count_du = 0
    # convert string to matrix
    test_mat = create_matrix(test_str)

    """ Compare each cell to the cells in the dutch and english matrix. 
        Give a point to the one with the highest percentage. """
    for x in range(len(test_mat)):
        for y in range(len(test_mat)):
            if test_mat[x][y] > 0:
                if en_matrix[x][y] > du_matrix[x][y]:
                    count_en += 1
                else:
                    count_du += 1

    # add the two counts up and use it to get an average score for each language
    total = count_en + count_du

    return {'dutch':  count_du / total, 'english': count_en / total}


def test(data: str, en_matrix: np.array, du_matrix: np.array) -> dict:
    # if data is just one sentence we will return it once
    try:
        # end results
        results = {'dutch': 0, 'english': 0}
        sentences = read_input(data)
        for sentence in sentences:
            # for each sentence get an answer. Take the highest outcome of the two answers and add that to the end result
            result = answer(sentence, en_matrix, du_matrix)
            outcome = max(result, key=lambda key: result[key])

            results[outcome] += 1

        return results

    except FileNotFoundError:
        # data is a string so we only return the answer function to show the percentage of english or dutch
        return answer(data, en_matrix, du_matrix)

