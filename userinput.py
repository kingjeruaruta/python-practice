
name = input("Enter your name: ")
print(f"Hello, {name}!\n")

number1 = int(input("Enter first no.   : "))
number2 = int(input("Enter second no.  : "))

add = number1 + number2 
sub = number1 - number2
mul = number1 * number2
div = number1 / number2
rem = number1 % number2


print(f"\nSum         : {add} \nDifference  : {sub} \nProduct     : {mul} \nQuotient    : {div} \nRemainder   : {rem}")


print("\n === CALCULATOR === ")
num1 = float(input("\Enter first no.          : "))
num2 = float(input("Enter second no.         : "))
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

print("Result                      :", result)