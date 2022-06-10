from ast import operator
from unittest import result
from replit import clear

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add_number(num1, num2):
    return num1 + num2

def substract_number(num1, num2):
    return num1 - num2

def multiply_number(num1, num2):
    return num1 * num2

def divided_number(num1, num2):
    return num1 / num2

operators = {
    "+": add_number,
    "-": substract_number,
    "*": multiply_number,
    "/": divided_number
}

def calculator():
    print(logo)
    
    number1 = float(input("What's the first number?: "))
    for symbol in operators:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("What's the next number?:"))

        calc_function = operators[operation_symbol]
        result = calc_function(number1, number2)

        print(f"{number1} {operation_symbol} {number2} = {result}")

        continue_ans = input(f"Type 'y' to continue calclating with {result}, or type 'n' to start a new calculation: ")
        if continue_ans == "y":
            number1 = result
        elif continue_ans == "n":
            should_continue = False
            clear()
            calculator()
        else:
            should_continue = False
            print("Wrong choice!")

calculator()