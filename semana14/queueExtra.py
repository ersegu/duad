


class Node:
    data: str
    next: Node

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    head :"Node"
    
    def __init__(self, head=None):
        self.head = head

    def enqueue(self, node:Node):
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        print("Node added")
    
    def dequeue(self):
        if self.head is None:
            return None
        else: 
            data = self.head.data
            print(f"Node removed")
            self.head = self.head.next
            return data
        
    def print_all(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


queue = Queue()

queue.enqueue(Node("A"))
queue.enqueue(Node("B"))
queue.enqueue(Node("C"))

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

