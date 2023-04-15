# Calculator 1v2.0
# System Update: User input multiple numbers

def calculator():
    number1 = float(input("Enter a Number: "))

    while True:
        operator = input("Enter operator: ")
        if operator == "=":
            return number1

        another_number = float(input("Enter Another Number "))
        if operator == "+":
            number1 += another_number

        elif operator == "-":
            number1 -= another_number

        elif operator == "*":
            number1 *= another_number

        elif operator == "/":
            number1 /= another_number
        else:
            return "Invalid"


result = calculator()
print(result)