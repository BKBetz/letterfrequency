from mapper import mapper
from reducer import onebyonereduce

english_matrix = onebyonereduce(mapper('data/alice.txt'))
print(english_matrix)