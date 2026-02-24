
def case_counter(my_string):
    lower_case_counter = 0
    upper_case_counter = 0
    for char in my_string:
        if char.isupper(): 
            upper_case_counter += 1
        else:
            lower_case_counter += 1

    print("There's", upper_case_counter, "upper cases and", lower_case_counter, "lower cases")


case_counter("I love Nacion Sushi")

