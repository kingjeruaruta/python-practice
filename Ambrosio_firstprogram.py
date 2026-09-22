"""
Python Basics Activity
Author: Reign Ambrosio
Covers: Hello World, 5 Things About Me, Name & Age, Basic Operators,
        and an Advanced Calculator with extra features.
"""


print("=" * 50)
print("1. HELLO WORLD")
print("=" * 50)
print("Hello, World!")
print()


print("=" * 50)
print("2. FIVE THINGS ABOUT ME")
print("=" * 50)

five_things = [
    "I love women.",
    "I love McDo staff especially melai.",
    "We have a dog named cedric.",
    "I love pussy cats.",
    "I love Linux."
]

for i, fact in enumerate(five_things, start=1):
    print(f"{i}. {fact}")
print()


print("=" * 50)
print("3. NAME AND AGE")
print("=" * 50)

name = "Reign Ambrosio"
age = 24  

print(f"My name is {name} and I am {age} years old.")
print()


print("=" * 50)
print("4. BASIC ARITHMETIC OPERATORS")
print("=" * 50)

num1 = 10
num2 = 3

print(f"num1 = {num1}, num2 = {num2}")
print(f"Addition (+):       {num1} + {num2} = {num1 + num2}")
print(f"Subtraction (-):    {num1} - {num2} = {num1 - num2}")
print(f"Multiplication (*): {num1} * {num2} = {num1 * num2}")
print(f"Division (/):       {num1} / {num2} = {num1 / num2:.2f}")
print(f"Modulo (%):         {num1} % {num2} = {num1 % num2}")
print()



def advanced_calculator():
    print("=" * 50)
    print("5. ADVANCED CALCULATOR")
    print("=" * 50)
    print("Available operations:")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Modulo         (%)")
    print("  6. Exponent       (**)")
    print("  7. Square Root    (√)")
    print("  0. Exit")
    print()

    history = []  

    while True:
        choice = input("Choose an operation (0-7): ").strip()

        if choice == "0":
            print("\nCalculation History:")
            if not history:
                print("  (no calculations yet)")
            for entry in history:
                print(f"  {entry}")
            print("\nExiting calculator. Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
            print("Invalid choice. Please try again.\n")
            continue

        try:
            if choice == "7": 
                x = float(input("Enter a number: "))
                if x < 0:
                    print("Error: Cannot get the square root of a negative number.\n")
                    continue
                result = x ** 0.5
                entry = f"√{x} = {result}"
            else:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

                if choice == "1":
                    result = x + y
                    symbol = "+"
                elif choice == "2":
                    result = x - y
                    symbol = "-"
                elif choice == "3":
                    result = x * y
                    symbol = "*"
                elif choice == "4":
                    if y == 0:
                        print("Error: Division by zero is not allowed.\n")
                        continue
                    result = x / y
                    symbol = "/"
                elif choice == "5":
                    if y == 0:
                        print("Error: Modulo by zero is not allowed.\n")
                        continue
                    result = x % y
                    symbol = "%"
                elif choice == "6":
                    result = x ** y
                    symbol = "**"

                entry = f"{x} {symbol} {y} = {result}"

            print(f"Result: {result}\n")
            history.append(entry)

        except ValueError:
            print("Invalid input. Please enter numeric values.\n")


if __name__ == "__main__":
    advanced_calculator()