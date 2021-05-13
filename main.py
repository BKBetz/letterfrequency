from letterfrequency.mapper import mapper
from letterfrequency.reducer import onebyonereduce
from letterfrequency.matrix_test import answer

english_matrix = onebyonereduce(mapper('../data/alice.txt'))
dutch_matrix = onebyonereduce(mapper('../data/bzt.txt'))
test = "my banana is krom omdat brandon is a lazy varken"
print(answer(test, english_matrix, dutch_matrix))