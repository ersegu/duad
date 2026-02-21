
my_global_variable = "Hello World"

def my_function():
    my_variable = "Hello"

# Research https://www.w3schools.com/python/python_variables_global.asp

def my_other_function():
    global my_global_variable
    print("Old value: ", my_global_variable)
    my_global_variable = "My variable has changed"
    print("New value: ",my_global_variable)

##print(my_variable) 
##Gives error >> NameError: name 'my_variable' is not defined

my_other_function()




