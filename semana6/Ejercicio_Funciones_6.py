
def arrange_string(mystring):
    new_list = mystring.split("-")
    new_list.sort()
    new_string = ""
    for word in new_list:
        new_string += word + "-"

    new_string = new_string.strip("-")
    return new_string


print(arrange_string("python-variable-funcion-computadora-monitor"))


