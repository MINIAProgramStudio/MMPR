import os
import PyTaCo
import copy

def input_matrix():
    os.system('cls')
    print("Введіть розмір матриці:")
    while True:
        try:
            matrix_size = int(input(">>>"))
            break
        except:
            print("Невірний ввід, спробуйте ще раз")
    matrix = []
    for pos_y in range(matrix_size):
        matrix.append([])
        for pos_x in range(matrix_size):
            matrix[-1].append(0)

    matrix = PyTaCo.PyTableConsole(matrix)
    for pos_y in range(matrix_size):
        for pos_x in range(matrix_size):
            matrix.contains[pos_x][pos_y] = "X"
            os.system('cls')
            print(matrix)
            print("Введіть елемент Х:")
            while True:
                try:
                    matrix.contains[pos_x][pos_y] = int(input(">>>"))
                    break
                except:
                    print("Невірний ввід, спробуйте ще раз")
    return matrix


def check_refl(matrix):
    for pos in range(len(matrix.contains)):
        if matrix.contains[pos][pos] == 0:
            return False
    return True

def check_antirefl(matrix):
    for pos_y in range(len(matrix.contains)):
        for pos_x in range(len(matrix.contains)):
            if matrix.contains[pos_x][pos_y]:
                if pos_x == pos_y:
                    return False
    return True

def check_sym(matrix):
    for pos_y in range(len(matrix.contains)):
        for pos_x in range(len(matrix.contains)):
            if not matrix.contains[pos_y][pos_x] == matrix.contains[pos_x][pos_y]:
                return False
    return True

def check_asym(matrix):
    for pos_y in range(len(matrix.contains)):
        for pos_x in range(len(matrix.contains)):
            if matrix.contains[pos_x][pos_y] and matrix.contains[pos_y][pos_x]:
                return False
    return True

def check_antisym(matrix):
    for pos_y in range(len(matrix.contains)):
        for pos_x in range(len(matrix.contains)):
            if matrix.contains[pos_x][pos_y] and matrix.contains[pos_y][pos_x] and not pos_x == pos_y:
                return False

def check_trans(matrix):
    for pos_y0 in range(len(matrix.contains)):
        for pos_x0 in range(len(matrix.contains)):
            for pos_y1 in range(len(matrix.contains)):
                for pos_x1 in range(len(matrix.contains)):
                    if matrix.contains[pos_x0][pos_y0] and matrix.contains[pos_x1][pos_y1] and not matrix.contains[pos_x0][pos_y1]:
                        return False
    return True

def RS(matrix):
    a = copy.copy(matrix)
    b = copy.copy(matrix)
    result = copy.copy(matrix)
    b.transpose()
    for pos_x in range(a.width()):
        for pos_y in range(a.height()):
            result.contains[pos_x][pos_y] = max(0, a.contains[pos_x][pos_y]-b.contains[pos_x][pos_y])
    return result

def find_max(matrix):
    matrix_op = copy.deepcopy(matrix)
    matrix_op = RS(matrix_op)
    elements = [i for i in range(len(matrix_op.contains))]
    result = []
    for el in elements:
        good = True
        for i in range(len(matrix_op.contains)):
            if (not matrix_op.contains[i][el]) and matrix_op.contains[el][i]:
                good = False
        if good:
            result.append(el)
    return result

def find_best(matrix):
    elements = [i for i in range(len(matrix.contains))]
    result = []
    for el in elements:
        good = True
        for i in range(len(matrix.contains)):
            if not matrix.contains[i][el]:
                good = False
        if good:
            result.append(el)
    return result

def find_worst(matrix):
    elements = [i for i in range(len(matrix.contains))]
    result = []
    for el in elements:
        good = True
        for i in range(len(matrix.contains)):
            if not matrix.contains[el][i]:
                good = False
        if good:
            result.append(el)
    return result
def find_min(matrix):
    matrix_op = copy.deepcopy(matrix)
    matrix_op = RS(matrix_op)
    elements = [i for i in range(len(matrix_op.contains))]
    result = []
    for el in elements:
        good = True
        for i in range(len(matrix_op.contains)):
            if (not matrix_op.contains[el][i]) and matrix_op.contains[i][el]:
                good = False
        if good:
            result.append(el)
    return result

def aug_matrix(matrix):
    new_matrix = copy.copy(matrix)
    for pos_x in range(len(new_matrix.contains)):
        for pos_y in range(len(new_matrix.contains)):
            if new_matrix.contains[pos_x][pos_y]:
                new_matrix.contains[pos_x][pos_y] = 0
            else:
                new_matrix.contains[pos_x][pos_y] = 1
    return new_matrix

def reverse_matrix(matrix):
    new_matrix = copy.copy(matrix)
    new_matrix.transpose()
    return new_matrix
def check_all(matrix):
    os.system('cls')
    print(matrix)
    print("Це відношення:")
    any = False
    if check_refl(matrix):
        print("рефлексивне")
        any = True
    if check_antirefl(matrix):
        print('антирефлексивне')
        any = True
    if check_sym(matrix):
        print('симетричне')
        any = True
    if check_asym(matrix):
        print('асиметричне')
        any = True
    if check_antisym(matrix):
        print('антисиметичне')
        any = True
    if check_trans(matrix):
        print('транзитивне')
        any = True
    if not any:
        print("не має вказаних властивостей")

    if find_best(matrix):
        print("Найкращі елементи: " + str(find_best(matrix)))
    else:
        print("Найкращі елементи відсутні")
    if find_worst(matrix):
        print("Найгірший елемент: " + str(find_worst(matrix)))
    else:
        print("Найгірші елементи відсутні")
    print("RS:")
    print(RS(copy.deepcopy(matrix)))
    if find_max(matrix):
        print("Максимальні елементи: " + str(find_max(matrix)))
    else:
        print("Максимальні елементи відсутні")
    if find_min(matrix):
        print("Мінімальні елементи: " + str(find_min(matrix)))
    else:
        print("Мінімальні елементи відсутні")
    print("Оберенене відношення:")
    print(reverse_matrix(matrix))
    print('Доповнене відношення:')
    print(aug_matrix(matrix))
    input("Continue>>>")



while True:
    check_all(input_matrix())