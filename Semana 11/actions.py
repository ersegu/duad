"""
This module contain the following functionalities for the the Student Control System:

1- Adding Students and their respective information (Name, Section, and Grades)
2- Seeing the information for all added students or imported students.
3- Seeing the top 3 students with best Average score.
4- Seeing the average score taking into consideration all students.
5 and 6 will be done in a different module handling the import and export of data.
7 - Deleting a student using their name and section.
8 - Seeing students who failed at least 1 subject.
"""

# Define The Class Student

class Student:
    def __init__(self,name, lastname,section,spanish_grade,english_grade,social_grade,science_grade,average):
        self.name = name
        self.lastname = lastname
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_grade = social_grade
        self.science_grade = science_grade
        self.average = average

    def __str__(self):
        return f"Student Full Name: {self.name} {self.lastname}, Section: {self.section}, Grades: Spanish: {self.spanish_grade}, English: {self.english_grade}, Social Studies: {self.social_grade}, Science: {self.science_grade}, Average Grade: {self.average}"


# Validation Methods

def is_valid_name(name):
    try:
        if name == "" or name == None:
            return False
        for char in name: 
            if char.isdigit():
                return False
        return True
    except Exception as ex:
        print(f"There has been an error validating the name: {ex}")


def is_valid_section(section):
    try:
        if len(section) < 2 or len(section) > 3:
            return False
        
        number_part = int(section[:-1])
        letter_part = section[-1]
        if number_part < 1 or number_part > 12:
            return False
        if not letter_part.isalpha():
            return False
        
        return True       
    except Exception as ex:
        print(f"There has been an error validating the section: {ex}")


def is_grade_valid(grade):
    try:
        if grade < 0 or grade > 100:
            return False
        return True
    except Exception as ex:
        print(f"Unable to validate grade: {ex}")


def find_student(name, lastname, section, student_list):
    try:
        for student in student_list:
            if student.name == name.title() and student.lastname == lastname.title() and student.section == section.upper():
                return student
    except AttributeError as ex:
        print(f"Unable to validate if student exists: {ex}")


def add_student(student_list):
    try:
        while True:
            while True:
                name = input("Enter the Student First Name\n")
                if not is_valid_name(name):
                    print("Name cannot be empty or contain numbers\n")
                else:
                    break
            
            while True:
                lastname = input("Enter the student's Last Name\n")
                if not is_valid_name(lastname):
                    print("Last Name cannot be empty or contain numbers\n")
                else:
                    break

            while True:
                section = input("Enter the student's section using the Following format: 1B or 10C\n")
                if not is_valid_section(section):
                    print("Invalid section. Use format as 11A or 1B\n")
                else:
                    break
            student = find_student(name, lastname,section, student_list)
            if student is None:
                while True:
                    spanish_grade = float(input("Enter the grade of the Spanish course\n"))
                    if not is_grade_valid(spanish_grade):
                        print("Grade has to be a value between 0 and 100\n")
                    else:
                        break
                
                while True:
                    english_grade = float(input("Enter the grade for the English course\n"))
                    if not is_grade_valid(english_grade):
                        print("Grade has to be a value between 0 and 100\n")
                    else: 
                        break

                while True:                          
                    social_grade = float(input("Enter the grade for the Social Studies course\n"))
                    if not is_grade_valid(social_grade):
                        print("Grade has to be a value between 0 and 100\n")
                    else:
                        break

                while True:
                    science_grade = float(input("Enter the grade for the Science course\n"))
                    if not is_grade_valid(science_grade):
                        print("Grade has to be a value between 0 and 100\n")
                    else:
                        break
                average = (spanish_grade + english_grade + social_grade + science_grade) / 4
                student = Student(name.title(),lastname.title(),section.upper(),spanish_grade,english_grade,social_grade,science_grade,average)
                student_list.append(student)
                print("Student added successfully into the system.")
                
                while True:
                    continue_loop = input("Do you want to add another student? y/n\n")
                    if continue_loop.lower() != 'y' and continue_loop.lower() != 'n':
                        print("Invalid Option. Please use Y or N\n")
                    else:
                        break
                if continue_loop.lower() == 'n':
                    break
            else: 
                print("Student already exists.")
                break
    except (ValueError, TypeError, AttributeError) as ex:
        print(f"Unable to add student: {ex}")
    except ArithmeticError as ex:
        print(f"Unable to get average for student's grades: {ex}")


def print_student_information(student_list): 
    try:
        for student in student_list:
            print(student)
    except(IndexError, AttributeError) as ex:
        print(f"Unable to print student information: {ex}")


def print_top_3_students(student_list):
    try:
        sorted_list = sorted(student_list,key=sort_by_average, reverse=True)
        top_students = sorted_list[:3]
        print(f"The 3 stop students are:\n")
        for student in top_students:
            print(student)
    except (IndexError,ValueError,AttributeError, TypeError) as ex:
        print(f"Unable to get Top 3 students")


def sort_by_average(student):
    return student.average


def print_grade_average(student_list):
    counter = 0
    average = 0
    try:
        for student in student_list:
            average += student.average
            counter += 1
        average = average / counter
        print(f"The average grade is: {average}")
    except (TypeError, AttributeError, ArithmeticError) as ex:
        print(f"Unable to calculate average: {ex}")


def delete_student(student_list):
    try:
        while True:
            name = input("Enter the name of the student you want to delete:\n")
            if not is_valid_name(name):
                print("Name cannot be empty or contain numbers\n")
            else:
                break
                
        while True:
            lastname = input("Enter the last name of the student you want to delete:\n")
            if not is_valid_name(lastname):
                print("Last Name cannot be empty or contain numbers\n")
            else:
                break

        while True:
            section = input("Enter the section of the student you want to delete (Use the following format: 1B or 10C):\n")
            if not is_valid_section(section):
                print("Invalid section. Use format as 11A or 1B\n")
            else:
                break
        student_to_delete = find_student(name, lastname, section, student_list)
        if student_to_delete is not None:
            delete = input(f"Do you want to delete the student:\n{name} {lastname} from section {section}? Y/N\n")
            if delete.lower() == 'y':
                student_list.remove(student_to_delete)
                print("Student deleted successfully.")
        else: 
            print("Student not found")
    except (ValueError, AttributeError) as ex:
        print(f"Unable to delete student: {ex}")


def print_failed_students(student_list):
    failed_students = []
    try:
        for student in student_list:
            if float(student.spanish_grade) < 60 or float(student.english_grade) < 60 or float(student.social_grade) < 60 or float(student.science_grade) < 60:
                failed_students.append(student)
        print("The students that have at least 1 failed subject are:\n")
        for student in failed_students:
            print(student)
    except (IndexError,AttributeError,TypeError) as ex:
        print(f"Unable to get students with at least 1 failed subject.")