

class Node:
    data: str
    next: Node

    def __init__ (self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def insert_front(self, node:Node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_back(self, node:Node):
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def delete(self, data):
        if self.head is None:
            return None
        else:            
            if data == self.head.data:
                self.head = self.head.next
                print("Data removed")
            else:
                current_node = self.head
                while current_node.next is not None:
                    if current_node.next.data == data:  
                        print("Data removed")
                        current_node.next = current_node.next.next
                        break
                    current_node = current_node.next
        
    def print_all(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


def bubble_sort(linkedlist:LinkedList):
    __temp_list = []
    __current_node = linkedlist.head
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
    
    __linkedlist = LinkedList()
    for i in range(len(__temp_list)):
        node = __temp_list[i]
        node.next = None
        __linkedlist.insert_back(node)

    return __linkedlist



ll = LinkedList()

ll.insert_front(Node(10))
ll.insert_front(Node(20))


ll.insert_back(Node(30))
ll.insert_back(Node(40))

print("Before")
ll.print_all()

print("\nSorting Linked List")
ll = bubble_sort(ll)

print("\nAfter")
ll.print_all()

