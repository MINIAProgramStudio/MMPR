import PythonTableConsole as PyTaCo
import os

def round_to(number, digits = 4):
    return int(number*10**digits)/10**digits

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
            print("Введіть коефіцієнт матриці #"+str(i+1)+":")
            while True:
                try:
                    self.coefficients.append(float(input(">>>")))
                    break
                except:
                    print("Невірний ввід, спробуйте ще раз")
        self.input_complete = True

    def print(self):
        if self.input_complete:
            for i in range(self.number_of_matrixes):
                print(self.coefficients[i])
                print(self.matrixes[i])
        else:
            print("Задача не задана повністю")

    def solve(self):
        if not self.input_complete:
            return 0

        print("Розв'язок:")
        # розрахувати перетин вхідних відношень
        matrix = []
        for i in range(self.number_of_variables):
            matrix.append([])
            for ii in range(self.number_of_variables):
                min_value = 1
                for iii in range(self.number_of_matrixes):
                    value = float(self.matrixes[iii].contains[i][ii])*float(self.coefficients[iii])
                    if value < min_value:
                        min_value = value
                matrix[i].append(round_to(min_value))
        crossection = PyTaCo.PythonTableConsole(matrix)
        print("Перетин вхідних відношень:")
        print(crossection)


        # розрахувати нечітку підмножину недомінованих альтернатив перетину
        notdom_1 =[]
        for i in range(self.number_of_variables):
            sup = 0
            for ii in range(self.number_of_variables):
                value = float(crossection.contains[i][ii]) - float(crossection.contains[ii][i])
                if value > sup: sup = max(min(value, 1), 0)
            notdom_1.append([round_to(1-sup)])
        notdom_1 = PyTaCo.PythonTableConsole(notdom_1)
        print("Недоміновані альтернативи 1:")
        print(notdom_1)

        # адитивна згортка відношень
        matrix = []
        for i in range(self.number_of_variables):
            matrix.append([])
            for ii in range(self.number_of_variables):
                value = 0
                for iii in range(self.number_of_matrixes):
                    value += float(self.matrixes[iii].contains[i][ii]) * float(self.coefficients[iii])
                matrix[i].append(round_to(value))

        addition = PyTaCo.PythonTableConsole(matrix)
        print("Адитивна згортка вхідних відношень:")
        print(addition)

        # розрахувати нечітку підмножину недомінованих альтернатив аддитивної згортки
        notdom_2 = []
        for i in range(self.number_of_variables):
            sup = 0
            for ii in range(self.number_of_variables):
                value = float(addition.contains[i][ii]) - float(addition.contains[ii][i])
                if value > sup: sup = max(min(value, 1), 0)
            notdom_2.append([round_to(1-sup)])
        notdom_2 = PyTaCo.PythonTableConsole(notdom_2)
        print("Недоміновані альтернативи 2:")
        print(notdom_2)

        # перетин недомінованих альтернатив
        results = []
        for i in range(self.number_of_variables):
            matrix.append([])
            if notdom_1.contains[i][0] < notdom_2.contains[i][0]:
                results.append(round_to(notdom_1.contains[i][0]))
            else:
                results.append(round_to(notdom_2.contains[i][0]))
        print("Перетин недомінованих альтернатив:")
        print(results)

        return results.index(max(results))