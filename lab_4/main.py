import PythonTableConsole as PyTaCo
from Problem import Problem
import os

def loop():
    test_prob = Problem(int(input("Кількість змінних>>>")), int(input("Кількість відношень>>>")))
    test_prob.input()
    os.system('cls')
    print("Умова:")
    test_prob.print()
    print(test_prob.solve())
while True:
    try:
        loop()
    except:
        print("сталося щось дивне")
        input("Натисніть будь-яку клавішу щоб продовжити")
        os.system("cls")