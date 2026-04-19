

class Node:
    def __init__ (self, data: str, next=None):
        self.data =  data
        self.next = next


class Queue:
    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def enqueue(self,node):
        current_node = self.head
        while (current_node.next is not None):
            current_node = current_node.next
        current_node.next = node

    def dequeue(self):
        self.head = self.head.next

third_node = Node("I'm the third")
second_node = Node("I'm the second", third_node)
first_node = Node("I'm the first", second_node)

queue = Queue(first_node)

print("Adding a node")

queue.enqueue(Node("I'm the new node"))
queue.print_structure()

print("Removing a node")
queue.dequeue()

queue.print_structure()
