import PythonTableConsole as PyTaCo

class Problem:
    def __init__(self, number_of_variables = 5, number_of_matrixes = 2):
        self.number_of_variables = number_of_variables
        self.number_of_matrixes = number_of_matrixes
        self.input_complete = False
        self.matrixes = None
        self.solution = None
