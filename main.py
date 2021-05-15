from mapper import mapper
from reducer import onebyonereduce
from matrix_test import test


def main(pathToEnglishTxtFile, pathToDutchTxtFile, testStringOrFile):
    english_matrix = onebyonereduce(mapper(pathToEnglishTxtFile))
    dutch_matrix = onebyonereduce(mapper(pathToDutchTxtFile))
    result = test(testStringOrFile, english_matrix, dutch_matrix)
    print(result)

main("data/alice.txt", "data/bzt.txt", "my banana is krom omdat brandon is a lazy varken")
