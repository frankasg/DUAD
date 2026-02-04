    
class Node:
    data: str
    left_node: "Node"
    right_node: "Node"

    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


class BinaryTree:
    root: Node

    def __init__(self, root: Node):
        self.root = root

    def print_structure(self, node=None):
        current_node = self.root if node is None else node

        print(current_node.data)
        
        if current_node.left_node is not None:            
            self.print_structure(current_node.left_node)
        
        if current_node.right_node is not None:            
            self.print_structure(current_node.right_node)


# Nivel 3 (hojas)
h = Node("H")
i = Node("I")
j = Node("J")
f = Node("F")
g = Node("G")

# Nivel 2
d = Node("D", left_node=h, right_node=i)
e = Node("E", left_node=j)

# Nivel 1
b = Node("B", left_node=d, right_node=e)
c = Node("C", left_node=f, right_node=g)

# Nivel 0 (raíz)
a = Node("A", left_node=b, right_node=c)

# Árbol
tree = BinaryTree(a)
tree.print_structure()



