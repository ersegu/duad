
# Version 1 = O(N)

def manual_add(n):  
    result = 0 
    for i in range(1, number + 1): # O(N)
        result += i
    return result

# Version 2 = O(1)

def add_formula(n):
    return number * (number + 1) // 2 # O(1)

"""
¿Cuál es la complejidad de cada versión?
R> Version 1 has a complexity of O(N) due to the for loop. And version 2 has a complexity of O(1).

¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
R>> I would use version 2 due to the lowest complexity and since it uses a mathematic formula to get to the same result, 
which makes it more efficient as the number grows larger. Version 1 would require basically the same amount of iterations as the number. 
"""