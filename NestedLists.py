"""
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the
name(s) of any student(s) having the second lowest grade.

Short Code
-----------------------------------------------------------------------------------------
students = []

for _ in range(int(input())):
    name = input()
    score = float(input())

    students.append([name, score])
students = sorted(students, key=lambda x: x[1])
second_highest = students[0][1]
for name, grade in students:
    if grade > second_highest:
        second_highest = grade
        break
print('\n'.join([name for name, grade in sorted(students) if grade == second_highest]))
-----------------------------------------------------------------------------------------
"""

students = []

for _ in range(int(input())):
    name = input()
    score = float(input())

    students.append([name, score])


min = None
for i in range(2):
    min = students[0][1]
    for index, score in enumerate(students):
        if float(score[1]) < min:
            min = float(score[1])

    if i == 0:
        index = 0
        while index < len(students):
            if students[index][1] == min:
                del students[index]
                index = 0
            else:
                index += 1

a = []
for index, score in enumerate(students):
    if score[1] == min:
        a.append(score[0])

a = sorted(a)
for i in a:
    print(i)

