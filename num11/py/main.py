from math import sqrt
import numpy as np

data = {'a': (0.6, 1.9),
        'b': (1.8, 1.6),
        'c': (2.7, 2.0),
        'd': (3.0, 2.1),
        'e': (3.1, 2.6),
        'f': (3.1, 4.5),
        'g': (3.8, 0.6),
        'h': (4.2, 2.7)
        }

log = []


def Single_link():
    n = len(data)
    matrix = [[] * n] * n
    i = 0
    for k in data.keys():
        matrix[i] = calc_cos_sim_with(k)
        i += 1
    print(matrix)
    k1 = 0
    for i in matrix:
        k2 = 0
        for j in i:
            if k2 > k1:
                matrix[k1][j] = 0
            k2 += 1
        k1 += 1

    for i in range(n - 1):
        index = arg_min_matrix(matrix)
        matrix = update_matrix(matrix, index)
    print(matrix)
    print(log)


def update_matrix(matrix, index: tuple):
    # matrix = np.delete(matrix, index[0], axis = 0)
    row1 = index[0]
    row2 = index[1]
    name = index[1]
    temp_lst = []
    log.append(name)
    for i in matrix[row1]:
        temp_lst.append({name + i: min(matrix[row1][i], matrix[len(matrix)-1][i])})
    matrix = np.delete(matrix, row1, axis=0)
    matrix = np.delete(matrix, row2, axis=0)
    matrix = np.insert(matrix, len(matrix), temp_lst, axis=0)

    return matrix


def arg_min_matrix(matrix) -> tuple:
    min_ = matrix[0]['aa']
    n = range(len(matrix))
    index = (0, 0)
    k = 0
    for i in matrix:
        for j in i:
            if (i[j] < min_) and (i[j] != 0):
                min_ = i[j]
                index = (k, j)
        k += 1
    return index


def calc_cos_sim_with(name: str) -> map:
    map_ = {}
    target = data[name]
    for k_i, v_i in data.items():
        map_[k_i + name] = cos_sim(v_i, target)
    return map_


def cos_sim(vec_1: tuple, vec_2: tuple) -> float:
    sum_ = 0
    for i in range(len(vec_1)):
        sum_ += vec_1[i] * vec_2[i]
    return sum_ / (vec_len(vec_1) * vec_len(vec_2))


def vec_len(vec: tuple) -> float:
    return sqrt(vec[0] ** 2 + vec[1] ** 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Single_link()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
