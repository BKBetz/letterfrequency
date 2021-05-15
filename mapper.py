from letterfrequency.matrix import create_matrix
from letterfrequency.matrix_test import read_input


def mapper(file_input: str) -> []:
    """Create for each line an matrix and send this to the reduce function"""
    data = read_input(file_input)

    matrix = [create_matrix(x) for x in data]
    return matrix