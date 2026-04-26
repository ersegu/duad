


def bubble_sort(list):
    steps = 0
    interchanges = 0
    for j in range(0,len(list)-1):
        for i in range(0, len(list)-1-j):
            steps += 1
            current_item = list[i]
            next_item = list[i+1]
            if current_item > next_item:
                interchanges += 1
                list[i] = next_item
                list[i+1] = current_item
    print("Sorted List: ",list)
    print("Iterations: ",steps)
    print("Interchanges: ",interchanges)


list = [5,4,3,2,1]

bubble_sort(list)


