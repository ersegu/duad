


def linear_search(my_list, target):  # O(N)
    for item in my_list: # O(N)
        if item == target: # O(1)
            return True # O(1)
    return False # O(1)


def binary_search(my_list, target): # O(logN)
    low = 0 # O(1)
    high = len(my_list) - 1 # O(1)
    while low <= high: # O(logN)
        mid = (low + high) // 2 # O(1)
        if my_list[mid] == target: # O(1)
            return True # O(1)
        elif my_list[mid] < target: # O(1)
            low = mid + 1 # O(1)
        else: # O(1)
            high = mid - 1 # O(1)
    return False # O(1)

"""
¿Cuál es la complejidad de cada algoritmo?
R>> linear_search has a complexity of O(N) due to the Loop. Binary search has a complexity of O(logN) due to the while loop reduces the search space in each iteration.
¿En qué condiciones conviene usar cada uno?
R>> Linear search might be useful if working with small lists. As the items in the list increase so the number of iterations.
Binary search can be useful on larger lists as it reduces the search space in each iteration making it more efficient.
¿Qué pasa si la lista no está ordenada?
R>> With linear search, it does not matter as it will have to iterate across all items in the list. With Binary search, it may fail to find the item even if it exist 
in the list. For binary search to work properly the list needs to be sorted first due to the logic it uses.
"""


list = [1,7,10,2,15]


found = binary_search(list, 2)

print(found)