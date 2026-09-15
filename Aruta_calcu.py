print("\n === BASIC CALCULATOR === ")
number1 = float(input("\nEnter first no.             : "))
number2 = float(input("Enter second no.            : "))

while True: 
    operator =   input("Enter operator (+, -, *, /) : ")

    if operator == "+":
        result = number1 + number2
        break
    elif operator == "-":
        result = number1 - number2
        break
    elif operator == "*":
        result = number1 * number2
        break
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Invalid"
        break
    else:
        print("Invalid operator, please try again!")

print("\nResult                      :", result)