print("\n === CALCULATOR === ")
num1 = float(input("Enter first no.             : "))
num2 = float(input("Enter second no.            : "))
oper =   input("Enter operator (+, -, *, /) : ")


if oper == "+":
    result = num1 + num2
elif oper == "-":
    result = num1 - num2
elif oper == "*":
    result = num1 * num2
elif oper == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Invalid"
else:
    result = "Invalid"

print("\nResult                      :", result)