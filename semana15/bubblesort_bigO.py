

def bubble_sort(list): 
    for j in range(0,len(list)-1): # O(N)
        for i in range(0, len(list)-1-j): # O(N^2) 
            current_item = list[i] # O(1)
            next_item = list[i+1] # O(1)
            if current_item > next_item: # O(1)
                list[i] = next_item # O(1)
                list[i+1] = current_item # O(1)

list = [5,4,3,2,1] # O(1)

bubble_sort(list) # O(N^2)

print(list) #O(1)
