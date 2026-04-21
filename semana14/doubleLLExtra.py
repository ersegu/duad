

class Node:
    data: str
    before: Node
    next: Node

    def __init__ (self, data, before=None, next=None):
        self.data = data
        self.before = before
        self.next = next


class DoubleLinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def append(self, node:Node):
        if self.tail is None:
            self.tail = node
            self.head = self.tail
        else:
            self.tail.next = node
            node.before = self.tail
            self.tail = node
        print("Node added in the back")

    def prepend(self, node:Node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.head.before = node
            node.next = self.head
            self.head = node
        print("Node added in the front")

    def delete(self, data):
        if self.head is None:
            return None
        else:
            if self.head == self.tail and data == self.head.data and data == self.tail.data:
                self.head = None
                self.tail = None
            elif data == self.head.data:
                self.head = self.head.next
                self.head.before = None
                print("Data removed")
            elif data == self.tail.data:
                self.tail = self.tail.before
                self.tail.next = None
                print("Data removed")
            else:
                current_node = self.head
                while current_node.next is not None:
                    if current_node.next.data == data:  
                        print("Data removed")
                        current_node.next.next.before = current_node
                        current_node.next = current_node.next.next
                        break
                    current_node = current_node.next
        
    def print_forward(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def print_backward(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.before


dll = DoubleLinkedList()

dll.append(Node("B"))
dll.append(Node("A"))
dll.append(Node("A"))

print("\nPrinting forward")
dll.print_forward()
print("\nPrinting backward")
dll.print_backward()

print(f"\nHead\n{dll.head.data}")
print(f"\nTail\n{dll.tail.data}")

dll.delete("A")

print("\nPrinting forward")
dll.print_forward()
print("\nPrinting backward")
dll.print_backward()