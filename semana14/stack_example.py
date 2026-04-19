
class Node:
    def __init__ (self, data: str, next=None):
        self.data =  data
        self.next = next


class Stack:
    def __init__(self, head):
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

third_node = Node("I'm the third")
second_node = Node("I'm the second", third_node)
first_node = Node("I'm the first", second_node)

stack = Stack(first_node)

print("Current Structure:")
stack.print_structure()

print("Adding a node")

stack.push(Node("I'm the new node"))
stack.print_structure()

print("Removing a node")
stack.pop()

stack.print_structure()
