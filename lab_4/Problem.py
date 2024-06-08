import PythonTableConsole as PyTaCo
import os

def input_matrix(matrix_size = 0):
    os.system('cls')
    if not matrix_size:
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

    matrix = PyTaCo.PythonTableConsole(matrix)
    for pos_y in range(matrix_size):
        for pos_x in range(matrix_size):
            matrix.contains[pos_x][pos_y] = "X"
            os.system('cls')
            print(matrix)
            print("Введіть елемент Х:")
            while True:
                try:
                    matrix.contains[pos_x][pos_y] = float(input(">>>"))
                    break
                except:
                    print("Невірний ввід, спробуйте ще раз")
    return matrix

class Problem:
    def __init__(self, number_of_variables = 5, number_of_matrixes = 2):
        self.number_of_variables = number_of_variables
        self.number_of_matrixes = number_of_matrixes
        self.input_complete = False
        self.matrixes = []
        self.coefficients = []
        self.solution = None

    def input(self, override = False):
        if self.input_complete and not override:
            return 0
        for i in range(self.number_of_matrixes):
            self.matrixes.append(input_matrix(self.number_of_variables))
        for i in range(self.number_of_matrixes):
            print("Введіть коефіцієнт матриці #"+str(i)+":")
            while True:
                try:
                    self.coefficients.append(int(input(">>>")))
                    break
                except:
                    print("Невірний ввід, спробуйте ще раз")

    def print(self):
        if self.input_complete:
            for i in range(self.number_of_matrixes):
                print(self.matrixes[i])
                print(self.coefficients[i])
        else:
            print("Задача не задана повністю")