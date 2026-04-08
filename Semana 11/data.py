"""
This module contains the logic for exporting to a CSV file and importing an previously exported CSV file.
"""

import csv
from actions import Student

def export_to_csv(student_list):
    dic_student_list = []
    try:
        for student in student_list:
            dict_student = {}
            dict_student = {'name': student.name, 'lastname': student.lastname, 'section': student.section, 'spanish':student.spanish_grade,'english':student.english_grade,'social':student.social_grade,'science': student.science_grade, 'average':student.average}
            dic_student_list.append(dict_student)

        with open('students.csv','w',encoding='utf-8') as file:
            writer = csv.DictWriter(file,dic_student_list[0].keys())
            writer.writeheader()
            writer.writerows(dic_student_list)
        print("Data exported successfully.")
    except (FileNotFoundError, PermissionError, OSError, UnicodeEncodeError, TypeError, KeyError, ValueError, AttributeError, csv.Error) as ex:
        print(f"Unable to export data to csv file: {ex}")


def import_from_csv():
    student_list = []
    try:
        with open('students.csv',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row['name'], row['lastname'], row['section'], float(row['spanish']),float(row['english']),float(row['social']),float(row['science']),float(row['average']))
                student_list.append(student)
        print("Information imported successfully.")
        return student_list
    except (FileNotFoundError, PermissionError, OSError, UnicodeDecodeError, TypeError, KeyError, ValueError, AttributeError, csv.Error) as ex:
        print(f"Unable to import data to csv file: {ex}")
