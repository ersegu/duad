
import csv


def read_csv(file_path):
    try:
        with open(file_path) as csv_file:
            reader = csv.reader(csv_file,dialect='excel')
            headers = next(reader)
            for row in reader:
                for index,item in enumerate(row):
                    print(f"{headers[index].title()}: {item}")
                print()            
    except (FileNotFoundError, PermissionError, OSError,UnicodeDecodeError,TypeError,ValueError,csv.Error) as ex:
        print(f"Unable to open csv file. {ex}")


read_csv('games.csv')