from letterfrequency.mapper import mapper
from letterfrequency.reducer import onebyonereduce
from letterfrequency.matrix_test import test


def main(pathToEnglishTxtFile, pathToDutchTxtFile, testStringOrFile):
    english_matrix = onebyonereduce(mapper(pathToEnglishTxtFile))
    dutch_matrix = onebyonereduce(mapper(pathToDutchTxtFile))
    result = test(testStringOrFile, english_matrix, dutch_matrix)
    print(result)

main("../data/alice.txt", "../data/nl.txt", "../data/sentences.nl-en.txt")
