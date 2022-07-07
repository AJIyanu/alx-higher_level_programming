#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
print("_______")
j_student_2 = student_2.to_json(['first_name', 'age'])
print("__________")
j_student_3 = student_2.to_json(['middle_name', 'age'])
print("________")

print(j_student_1)
print(j_student_2)
print(j_student_3)

