# Task 1: Create a Dictionary of Student Marks

student_mark = {'Alice':'85','Leo':'65', 'Harry':'70','Karan':'40'}                 # Creates a dictionary where student names are keys and their marks are values.

student_name = input('Enter the students name: ')                                   #  Asks the user to input a student's name.

if (student_name in student_mark)==True:                                            # Check for student’s name in dictionary.
    print('{}\'s marks: {}'.format(student_name,student_mark[student_name]))
else:
    print('Student not found.')