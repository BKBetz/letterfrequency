from mapper import mapper
from reducer import onebyonereduce
from matrix_test import test
import sys


def main(pathToEnglishTxtFile, pathToDutchTxtFile, testStringOrFile):
    english_matrix = onebyonereduce(mapper(pathToEnglishTxtFile))
    dutch_matrix = onebyonereduce(mapper(pathToDutchTxtFile))
    result = test(testStringOrFile, english_matrix, dutch_matrix)
    print(result)


if __name__ == "__main__":
    # test_data is either a path to an txt file or a single string
    for line in sys.stdin:
        # call the test function foreach line
        input = line.rstrip('\n')
        main("data/alice.txt", "data/nl.txt", input)

