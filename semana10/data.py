"""
This module contains the logic for exporting to a CSV file and importing an previously exported CSV file.
"""

import csv

def export_to_csv(student_list):
    try:
        with open('students.csv','w',encoding='utf-8') as file:
            writer = csv.DictWriter(file,student_list[0].keys())
            writer.writeheader()
            writer.writerows(student_list)
        print("Data exported successfully.")
    except (FileNotFoundError, PermissionError, OSError, UnicodeEncodeError, TypeError, KeyError, ValueError, AttributeError, csv.Error) as ex:
        print(f"Unable to export data to csv file: {ex}")


def import_from_csv():
    student_list = []
    student = {}
    try:
        with open('students.csv',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {'name': row['name'], 'lastname': row['lastname'], 'section':row['section'], 'spanish': float(row['spanish']),'english':float(row['english']),'social':float(row['social']),'science':float(row['science']), 'average':float(row['average'])}
                student_list.append(student)
                student = {}
        print("Information imported successfully.")
        return student_list
    except (FileNotFoundError, PermissionError, OSError, UnicodeDecodeError, TypeError, KeyError, ValueError, AttributeError, csv.Error) as ex:
        print(f"Unable to import data to csv file: {ex}")
