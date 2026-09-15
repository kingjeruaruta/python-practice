print("\n === CALCULATOR === ")
number1 = float(input("\nEnter first no.             : "))
number2 = float(input("Enter second no.            : "))
operator =   input("Enter operator (+, -, *, /) : ")


if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Invalid"
else:
    result = "Invalid"

print("\nResult                      :", result)