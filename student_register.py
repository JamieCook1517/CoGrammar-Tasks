no_of_students = int(input("Type how many students are registering for the exam (a number): "))

with open('reg_form.txt', 'w') as file:
    for i in range(no_of_students):
        student_id = input(f"Type in the student's ID number (student {i+1}/{no_of_students}): ")
        file.write(f"{student_id} .......\n")  # Writes student ID number (dotted line for students to sign on)

# Check the folder on which your terminal operated
# (It is recommended that your terminal is in the directory of this file)