from letterfrequency.matrix import create_matrix


eng_matrix = create_matrix("""Speaking100 English Sentences Used in Daily Life Grammarhere  1 Year Ago  1 Comment
FACEBOOK PREV ARTICLE NEXT ARTICLE 
Sentences examples, 100 English Sentences Used in Daily Life
100 English Sentences Used in Daily Life
English Sentences Used In Daily Life
There are some stereotypes that are used in daily life, at work, at school, in the hospital and many more. If we are just learning English, learning these stereotypes will add fluency to us when we live in English-speaking countries, speaking English in daily life.
Learning the most frequently used phrases while learning a new language is very useful for our competence in the language. Since these sentences are used frequently in daily life, they help us speak the language we learn fluently. We need to be familiar with patterns of common phrases because language is easier to use.""")

nl_matrix = create_matrix("""Ik liep eens door de markt en zag een snoepkraam. Bij deze snoepkraam verkocht de man pepersnoepjes die echt pittig waren
                          ik geloofde hier niks van en besloot er twee te kopen. De volgende twee uur bestond uit alleen maar pijn en ijsjes eten
                          omdat mijn mond verbrand was door snoep.""")


test_matrix_nl = create_matrix("hoi ik ben brandon hoe gaat het met iedereen met mij gaat het namelijk niet goed")
test_matrix_en = create_matrix("hello my name is brandon how is everyone doing i am not doing okay")

strom_test = create_matrix("my banana is krom omdat brandon is a lazy varken")

print(nl_matrix)

def answer(test_mat):
    en_count = 0
    nl_count = 0
    for x in range(len(test_mat)):
        for y in range(len(test_mat)):
            if test_mat[x][y] > 0:
                loss_en = eng_matrix[x][y] - test_mat[x][y]
                loss_nl = nl_matrix[x][y] - test_mat[x][y]
                if loss_en < loss_nl:
                    en_count += 1
                else:
                    nl_count += 1

    total = en_count + nl_count

    return [en_count/total, nl_count/total]


print(answer(strom_test))

#
# def test(text):
#
#
