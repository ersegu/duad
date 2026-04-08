"""
Module that contains the logic for the Menu for the Student Control System Program.
"""
import actions
import data

def menu():
    selected_option = 0
    message = """
    Welcome to the Student Control System.

    Please select an option:
    
    1- Add Student Information.
    2- See Student Information.
    3- See top 3 students with best Average score.
    4- See average score.
    5- Export Student Information to CSV.
    6- Import Student Information from previously exported CSV.
    7- Delete Student.
    8- See Students who failed a course.
    9- Exit the System.
    """
    student_list = []
    while True:
        try:
            selected_option = int(input(f"{message}\n"))
            if selected_option < 1 or selected_option > 9:
                raise ValueError ("Select options between 1 and 9")
            match selected_option:
                case 1:
                    actions.add_student(student_list)
                case 2:
                    actions.print_student_information(student_list)
                case 3:
                    if len(student_list) == 0:
                        print("There are no students in the system. Please add students first\n")
                    else: 
                        actions.print_top_3_students(student_list)
                case 4:
                    if len(student_list) == 0:
                        print("There are no students in the system. Please add students first\n")
                    else:
                        actions.print_grade_average(student_list)
                case 5: 
                    if len(student_list) == 0:
                        print("There are no students in the system. Please add students before attempting to export.")
                    else:
                        data.export_to_csv(student_list)
                case 6:
                    while True:
                        if len(student_list) > 0:
                            import_file = input("if you import a file now, you will loose all changes. Do you want to continue? Y/N\n")
                            if import_file.lower() == 'y':
                                student_list = data.import_from_csv()
                                break  
                        else:
                            student_list = data.import_from_csv()
                            break
                case 7: 
                    actions.delete_student(student_list)
                case 8:
                    actions.print_failed_students(student_list)
                case 9:
                    exit()
        except (ValueError, TypeError, AttributeError) as ex:
            print(f"Invalid option selected: {ex}")
        except KeyboardInterrupt:
            print("\nExiting system")
            exit()
