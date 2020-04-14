import random
import time

another_student = True
student_counter = 1
student_list = []

while (another_student == True):
    student = str(
        input('Type student {} name: '.format(student_counter))).title()
    student_list.append(student)
    student_counter += 1
    print(student_list)

    choice = str(input('Add more students (Y/N)? ')).upper()

    if(choice == 'Y'):
        print("YES!")
        another_student = True
    else:
        print("NO!")
        another_student = False

selected = random.choice(student_list)

print('System selected following student: {}'.format(selected))
