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

def find_max(matrix):
    elements = [i for i in range(len(matrix.contains))]
    result = []
    for el in elements:
        a_exists = False
        b_exists = False
        for a in range(len(matrix.contains)):
            if a != el and matrix.contains[el][a]:
                a_exists = True

        for b in range(len(matrix.contains)):
            if b != el and matrix.contains[b][el]:
                b_exists = True

        if a_exists and not b_exists:
            result.append(el)

    return result

def find_min(matrix):
    elements = [i for i in range(len(matrix.contains))]
    result = []
    for el in elements:
        a_exists = False
        b_exists = False
        for a in range(len(matrix.contains)):
            if a != el and matrix.contains[el][a]:
                a_exists = True

        for b in range(len(matrix.contains)):
            if b != el and matrix.contains[b][el]:
                b_exists = True

        if not a_exists and b_exists:
            result.append(el)

    return result

def aug_matrix(matrix):
    new_matrix = copy.copy(matrix)
    for pos_x in range(len(new_matrix.contains)):
        for pos_y in range(len(new_matrix.contains)):
            new_matrix.contains[pos_x][pos_y] = (new_matrix.contains[pos_x][pos_y]+1)%2

def reverse_matrix(matrix):
    new_matrix = copy.copy(matrix)
    for pos_x in range(len(new_matrix.contains)):
        for pos_y in range(len(new_matrix.contains)):
            new_matrix.contains[pos_x][pos_y] = matrix.contains[pos_y][pos_x]
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


    if len(find_max(matrix)) > 1:
        print("Максимальні елементи: " + str(find_max(matrix)))
    elif len(find_max(matrix)) == 1:
        print("Найбільший елемент: " + str(find_max(matrix)[0]))
    else:
        print("Максимальних елементів не існує")

    if len(find_min(matrix)) > 1:
        print("Мінімальні елементи: " + str(find_min(matrix)))
    elif len(find_min(matrix)) == 1:
        print("Найменший елемент: " + str(find_min(matrix)[0]))
    else:
        print("Мінімальних елементів не існує")

    print("Оберенене відношення:")
    print(reverse_matrix(matrix))
    print('Доповнене відношення:')
    print(aug_matrix(matrix))
    input("Continue>>>")



while True:
    check_all(input_matrix())