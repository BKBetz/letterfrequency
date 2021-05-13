from letterfrequency.mapper import mapper
from letterfrequency.reducer import onebyonereduce

english_matrix = onebyonereduce(mapper('../data/alice.txt'))
print(english_matrix)