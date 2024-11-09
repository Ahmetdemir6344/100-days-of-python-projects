calculator_ascii = """
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def sum(num1, num2):
    return int(num1 + num2)
def subtract(num1, num2):
    return int(num1 - num2)
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2


def calculator():
    print(calculator_ascii)
    stop = True
    while stop ==True:
        operations = {"+": sum
            , "-": subtract
            , "*": multiply
            , "/": divide
                      }
        num1=float(input("Enter the first number: "))
        for i in operations:
            print(i)
        operations_choice = input("choice operations: ")
        num2=float(input("Enter the second number: "))
        value =operations[operations_choice](num1,num2)
        print(f"{num1}{operations_choice}{num2} = {value}")
        do_you_want = input("Would you like to continue? (y/n): ")
        if do_you_want != "yes":
            stop = False

calculator()



