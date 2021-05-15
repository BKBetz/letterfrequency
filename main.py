from letterfrequency.mapper import mapper
from letterfrequency.reducer import onebyonereduce
from letterfrequency.matrix_test import answer


def read_input(file: str):
    """Read the given file and seperate per line"""
    with open(file) as f:
        # we use .read().splitlines() instead of .readlines() to remove "\n" in an easy way
        data = f.read().splitlines()

    return data

english_matrix = onebyonereduce(mapper('../data/alice.txt'))
dutch_matrix = onebyonereduce(mapper('../data/bzt.txt'))
test = "my banana is krom omdat brandon is a lazy varken"
print(answer(test, english_matrix, dutch_matrix))
