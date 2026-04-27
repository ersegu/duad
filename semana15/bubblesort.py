

def bubble_sort(list):
    for j in range(0,len(list)-1):
        for i in range(0, len(list)-1-j):
            current_item = list[i]
            next_item = list[i+1]
            if current_item > next_item:
                list[i] = next_item
                list[i+1] = current_item


def bubble_sort_backwards(list):
    for j in range(0,len(list)-1):
        for i in range(len(list)-1,0+j,-1):
            current_item = list[i]
            next_item = list[i-1]
            if current_item < next_item:
                list[i] = next_item
                list[i-1] = current_item




list = [5,4,3,2,1]

bubble_sort(list)
print(list)


list2 = [5,4,3,2,1]
bubble_sort_backwards(list2)

print(list2)