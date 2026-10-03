print("GRADE EVALUATOR")

studentname = input("Enter your full name: ")

print()
print("Enter your grades below: ")
print()

programming3 = int(input("Programming 3: "))
dsa = int(input("Data Structures and Algorithms: "))
os = int(input("Operating Systems: "))
dcan = int(input("Digital Communication and Networking: "))
rva = int(input("Reading in Visual Arts: "))

average = (programming3 + dsa + os + dcan + rva) / 5


if average >= 97:
    final = (1.00)
elif average >= 94:
    final = (1.25)
elif average >= 91:
    final = (1.50)
elif average >= 88:
    final = (1.75)
elif average >= 85:
    final = (2.00)
elif average >= 82:
    final = (2.25)
elif average >= 79:
    final = (2.50)
elif average >= 76:
    final = (2.75)
elif average >= 75:
    final = (3.00)
elif average >= 65:
    final = (5.00)
else:
    final = "Invalid (OVERLOAD, INC, WITHDRAWN, DROPPED)"

print()
print("Student's Name: ", studentname)

print("Final Grade Report: ")
print("Programming 3       :", programming3)
print("Data Structures and Algorithms:", dsa)
print("Operating Systems   :", os)
print("Digital Communication and Networking:", dcan)
print("Reading in Visual Arts:", rva)

print()
print("Average: ", average)
print("Final Grade: ", final)