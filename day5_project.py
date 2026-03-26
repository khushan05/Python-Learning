# Student Marks Analyzer

print("=== Student Marks Analyzer ===")

marks = []

n = int(input("How many students: "))

# taking input
for i in range(n):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

# calculations
total = 0
highest = marks[0]

for mark in marks:
    total += mark

    if mark > highest:
        highest = mark

average = total / n

# output
print("\n=== Result ===")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest Marks: {highest}")