

subject1 = float(input("Enter Marks for Subject 1: "))
subject2 = float(input("Enter Marks for Subject 2: "))
subject3 = float(input("Enter Marks for Subject 3: "))
subject4 = float(input("Enter Marks for Subject 4: "))
subject5 = float(input("Enter Marks for Subject 5: "))


highestMarks = subject1
lowestMarks = subject1


if subject2 > highestMarks:
    highestMarks = subject2
if subject3 > highestMarks:
    highestMarks = subject3
if subject4 > highestMarks:
    highestMarks = subject4
if subject5 > highestMarks:
    highestMarks = subject5


if subject2 < lowestMarks:
    lowestMarks = subject2
if subject3 < lowestMarks:
    lowestMarks = subject3
if subject4 < lowestMarks:
    lowestMarks = subject4
if subject5 < lowestMarks:
    lowestMarks = subject5


avg = (subject1 + subject2 + subject3 + subject4 + subject5) / 5

print(f"Highest: {highestMarks}")
print(f"Lowest: {lowestMarks}")
print(f"Average: {avg}")
