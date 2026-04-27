
class Node:
    def __init__ (self, data: str, next=None):
        self.data =  data
        self.next = next


class Stack:
    def __init__(self, head=None):
        self.head = head

    def print_structure(self):
        current_node = self.head
        
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push(self,node):
        node.next = self.head
        self.head = node

    def pop(self):
        self.head = self.head.next

def bubble_sort(stack:Stack):
    __temp_list = []
    __current_node = stack.head
    while __current_node is not None:
        __temp_list.append(__current_node)
        __current_node = __current_node.next
    
    for j in range(0,len(__temp_list) - 1):
        for i in range(0, len(__temp_list)-1-j):
            current_item = __temp_list[i]
            next_item = __temp_list[i+1]
            if current_item.data > next_item.data:
                __temp_list[i] = next_item
                __temp_list[i+1] = current_item
    
    __stack = Stack()
    for i in range(len(__temp_list)-1,-1,-1):
        __stack.push(__temp_list[i])

    return __stack

third_node = Node("third")
second_node = Node("second")
first_node = Node("first")
node = Node("kilo")

stack = Stack()

stack.push(first_node)
stack.push(second_node)
stack.push(third_node)
stack.push(node)

print("before:")
stack.print_structure()

print("\nSorting the Stack")
stack = bubble_sort(stack)

print("\nafter")
stack.print_structure()

