


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


def bubble_sort(queue:Queue):
    __temp_list = []
    __current_node = queue.head
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
    
    __queue = Queue()
    for i in range(len(__temp_list)):
        node = __temp_list[i]
        node.next = None
        __queue.enqueue(node)

    return __queue

queue = Queue()

queue.enqueue(Node("alpha"))
queue.enqueue(Node("foxtrot"))
queue.enqueue(Node("Beta"))

print("Before")
queue.print_all()

print("\nSorting Queue")
queue = bubble_sort(queue)

print("\nAfter")
queue.print_all()
