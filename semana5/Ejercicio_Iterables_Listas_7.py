# **Cree un programa que verifique si todos los elementos de una lista son positivos**

my_list = [3, 6, 0, -2, 4]
is_positive = True

for number in my_list:
    if(number<=0):
        is_positive = False
        break

if(is_positive):
    print("All numbers are positive++")
else:
    print("There's at least 1 negative number or a zero")
    

