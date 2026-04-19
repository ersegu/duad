

class Node:
    def __init__ (self, data: str, next=None):
        self.data =  data
        self.next = next


class DoubleQueue:
    def __init__(self, head):
        self.head = head
        self.tail = head

    def print_structure(self):
        current_node = self.head
        
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push_left(self,node):
        node.next = self.head
        self.head = node

    def push_right(self, node):
        self.tail = node
        current_node = self.head
        while (current_node.next is not None):
            current_node = current_node.next
        current_node.next = node
        

    def pop_left(self):
        self.head = self.head.next

    def pop_right(self):
        current_node = self.head

        while (current_node.next.next is not None):
            current_node = current_node.next

        current_node.next = None
        self.tail = current_node
        


third_node = Node("I'm the third")
second_node = Node("I'm the second", third_node)
first_node = Node("I'm the first", second_node)

doublequeue = DoubleQueue(first_node)

print("Current Structure:")
doublequeue.print_structure()

print("Adding a node to the left")

doublequeue.push_left(Node("I'm the new first"))
doublequeue.print_structure()

print("Adding a node to the right")

doublequeue.push_right(Node("I'm the new last"))
doublequeue.print_structure()


print("Removing a node to the left")
doublequeue.pop_left()
doublequeue.print_structure()

print("Removing a node to the right")
doublequeue.pop_right()
doublequeue.print_structure()