# Grade Evaluator
# (user input)
# Student Grades [PROG 3, RVA, DSA, DCAN, OS]
# get the average
# diplay corresponding grade
# display name and grade

print(" === GRADE EVALUATOR === ")

student_name = input("Enter full name: ")

print("Enter your Grades below:")
print("Type 0 if you have no grade")

programming_3 = int(input("Programming 3 : "))
rva           = int(input("RVA           : "))
dsa           = int(input("DSA           : "))
dcan          = int(input("DCAN          : "))
ds            = int(input("DS            : "))

grades = [programming_3, rva, dsa, dsa, dcan, ds]

if 0 in grades:
    final = "INC"
else:
    average = sum(grades) / 5

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
        print("Invalid (OVERLOAD, INC, WITHDRAWN, DROPPED)")



print(f"Student's Name : {student_name}")
print(f"Final Grade    : {final}")


