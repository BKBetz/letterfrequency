import numpy as np


def create_matrix(string):
    # create an matrix using all combinations and the given string
    lower_string = string.lower()

    combs = create_combinations()
    check_frequency(combs, lower_string)
    matrix = np.array([combs[i] for i in combs]).reshape((28, 28))
    return matrix


def create_combinations():
    # create all possible combinations (aa, ab, ac, etc)
    all = 'abcdefghijklmnopqrstuvwxyz !'
    combs = dict()
    for x in all:
        for y in all:
            combs[x+y] = 0

    return combs


def replace_special_chars(comb):
    characters = 'abcdefghijklmnopqrstuvwxyz !'

    # example a, -> a!
    if comb[0] in characters:
        new_comb = comb.replace(comb[1], "!")

    # example ,a -> !a
    elif comb[1] in characters:
        new_comb = comb.replace(comb[0], "!")

    # example 11 -> !!
    else:
        new_comb = comb.replace(comb, '!!')

    return new_comb


def check_frequency(combs, string):
    # check how many times a certain combination appears
    for x in range(len(string) - 1):
        comb = string[x] + string[x+1]
        if comb in combs:
            combs[comb] += 1
        else:
            # if a special character (?, 5, 8, etc) occurs use this function to replace that char with !
            new_comb = replace_special_chars(comb)

            combs[new_comb] += 1
