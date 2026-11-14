# Student Marks Calculator

name = input("Enter student name: ")

mark1 = int(input("Enter marks in Subject 1: "))
mark2 = int(input("Enter marks in Subject 2: "))
mark3 = int(input("Enter marks in Subject 3: "))
mark4 = int(input("Enter marks in Subject 4: "))
mark5 = int(input("Enter marks in Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5

print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if all(0 <= mark <= 100 for mark in
       [mark1, mark2, mark3, mark4, mark5]):
    if all(mark >= 35 for mark in
           [mark1, mark2, mark3, mark4, mark5]):
        print("Result: PASS")
    else:
        print("Result: FAIL")
else:
    print("Invalid marks! Enter marks between 0 and 100.")
