

class Node:
    data: str
    left: "Node"
    right: "Node"

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    root: Node

    def __init__(self, root):
        self.root = root

    def print_structure(self):

        current_node = self.root
        self.__print_data(current_node)

    def __print_data(self, node):

        if (node != None):
            print(node.data);
            for i in range(2):
                if(i == 0):
                    self.__print_data(node.left)
                else:
                    self.__print_data(node.right)


node5 = Node("I'm the fifth")
node4 = Node("I'm the fourth",node5)
node3 = Node("I;m the third")
node2 = Node("I'm the second", node4)
node1 = Node("I'm the first", node2, node3)

binary_tree = BinaryTree(node1)

binary_tree.print_structure()

