import PythonTableConsole as PyTaCo
from Problem import Problem
import os

def loop():
    test_prob = Problem(int(input("Кількість змінних>>>")), int(input("Кількість відношень>>>")))
    test_prob.input()
    os.system('cls')
    print("Умова:")
    test_prob.print()
    result = test_prob.solve()
    print("Номер найкращої альтернативи:")
    print(result + 1)
while True:
    try:
        loop()
    except:
        print("сталося щось дивне")
        input("Натисніть будь-яку клавішу щоб продовжити")
        os.system("cls")