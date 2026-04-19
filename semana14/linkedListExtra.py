

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
        print("Node added in the front")
        self.print_all()

    def insert_back(self, node:Node):
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        print("Node added in the back")
        self.print_all()

    def delete(self, data):
        current_node = self.head
        
        if data == self.head.data:
            self.head = self.head.next
            print("Data removed")
        else:
            while current_node is not None:
                if current_node.next.data == data:  
                    print("Data removed")
                    current_node.next = current_node.next.next
                    break
                current_node = current_node.next
        self.print_all()
        
    def print_all(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


ll = LinkedList()

ll.insert_front(Node(10))
ll.insert_front(Node(20))


ll.insert_back(Node(30))
ll.insert_back(Node(40))


ll.delete(40)