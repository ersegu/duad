

class Node:
    def __init__ (self, data: str, next=None):
        self.data =  data
        self.next = next


class DoubleQueue:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def print_structure(self):
        if self.head is None:
            print("Queue is empty")
        
        else: 
            current_node = self.head
            
            while (current_node is not None):
                print(current_node.data)
                current_node = current_node.next

    def push_left(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def push_right(self, node):
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            current_node = self.head
            while (current_node.next is not None):
                current_node = current_node.next
            current_node.next = node
            self.tail = node
        
    def pop_left(self):
        if self.head is None:
            return None
        elif self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
            if self.head.next is None:
                self.tail = self.head

    def pop_right(self):
        if self.tail is None:
            return None
        elif self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            current_node = self.head

            while (current_node.next is not None):
                if current_node.next.next is None:
                    self.tail = current_node
                    self.tail.next = None
                    break
                current_node = current_node.next


def bubble_sort(doubleQ:DoubleQueue):
    __temp_list = []
    __current_node = doubleQ.head
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
    
    __doubleQ = DoubleQueue()
    for i in range(len(__temp_list)-1,-1,-1):
        node = __temp_list[i]
        node.next = None
        __doubleQ.push_left(node)

    return __doubleQ


# third_node = Node("I'm the third")
# second_node = Node("I'm the second", third_node)
# first_node = Node("I'm the first", second_node)

doublequeue = DoubleQueue()

doublequeue.push_left(Node("first"))
doublequeue.push_left(Node("second"))
doublequeue.push_left(Node("third"))
doublequeue.push_right(Node("Kilo"))
doublequeue.push_right(Node("kilo"))


print("Before")
doublequeue.print_structure()

print("\nSorting the Double Queue")
doublequeue = bubble_sort(doublequeue)

print("\nAfter")
doublequeue.print_structure()


