

def bubble_sort(list:list):
    def __validate_list():
        if len(list) == 0:
            raise ValueError ("List is empty")
        for item in list:
            if not str(item).isnumeric():
                raise ValueError ("Unable to sort list. It contains items that are not numeric")
        return True
    
    if __validate_list():  
        for j in range(0,len(list)-1):
            for i in range(0, len(list)-1-j):
                current_item = list[i]
                next_item = list[i+1]
                if current_item > next_item:
                    list[i] = next_item
                    list[i+1] = current_item



try:
    list = [5,3,4,2,1,7]
    list2 = []
    bubble_sort(list)
    print(list)
    bubble_sort(list2)
except ValueError as ex:
    print(ex)


