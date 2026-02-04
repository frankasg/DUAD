class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    top: Node

    def __init__(self, top=None):
        self.top = top

    def push(self, new_node: Node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            popped_node = self.top
            self.top = self.top.next
            return popped_node #este return no lo estoy usando porque no era la idea de ejercicios si no mas bien como para demostrar que un pop debería retorna el método al que se le hace pop

    def print_structure(self):
        current_node = self.top

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

print("--------- PUSH --------")
first_node = Node("first")
my_stack = Stack(first_node)

second_node = Node("second")
my_stack.push(second_node)

second_node = Node("third")
my_stack.push(second_node)
my_stack.print_structure()

print("--------- POP --------")
my_stack.pop()
my_stack.print_structure()

print("--------- POP --------")
my_stack.pop()
my_stack.print_structure()

print("--------- POP --------")
my_stack.pop()
my_stack.print_structure()

print("--------- POP --------")
my_stack.pop()
my_stack.print_structure()

