from letterfrequency.matrix import create_matrix


def read_input(file: str):
    """Read the given file and seperate per line"""
    with open(file) as f:
        # we use .read().splitlines() instead of .readlines() to remove "\n" in an easy way
        data = f.read().splitlines()

    return data


def mapper(file_input: str):
    """Create for each line an matrix and send this to the reduce function"""
    data = read_input(file_input)

    for x in data:
        matrix = create_matrix(x)




mapper('../data/alice.txt')
