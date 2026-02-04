class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleEndedQueue:
    head: Node

    def __init__(self, head=None):
        self.head = head    

    def push_left (self, new_node: Node):
        new_node.next = self.head
        self.head = new_node    

    def push_right (self, new_node):
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
    
    def pop_right(self):
        popped_node = None
        if self.head is None:
            return None  
        
        if self.head.next == None:
            popped_node = self.head
            self.head = None
            return popped_node
        
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next

        popped_node = current_node.next
        current_node.next = None
        return popped_node

    def pop_left(self):
        if self.head == None:
          return None
        
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node #Igual al ejercicio 1 hago este return como para demostrar como sería un pop real 


    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


node4 = Node("4")
my_DoubleEndedQueue = DoubleEndedQueue(node4)

print("--------- PUSH RIGHT--------")
node5 = Node("5")
my_DoubleEndedQueue.push_right(node5)

node6 = Node("6")
my_DoubleEndedQueue.push_right(node6)
my_DoubleEndedQueue.print_structure()

print("--------- PUSH LEFT--------")
node3 = Node("3")
my_DoubleEndedQueue.push_left(node3)

node2 = Node("2")
my_DoubleEndedQueue.push_left(node2)

node1 = Node("1")
my_DoubleEndedQueue.push_left(node1)
my_DoubleEndedQueue.print_structure()

print("--------- POP LEFT --------")
my_DoubleEndedQueue.pop_left()
my_DoubleEndedQueue.pop_left()
my_DoubleEndedQueue.pop_left()
my_DoubleEndedQueue.print_structure()

print("--------- POP RIGHT --------")
my_DoubleEndedQueue.pop_right()
my_DoubleEndedQueue.print_structure()

print("--------- POP RIGHT --------")
my_DoubleEndedQueue.pop_right()
my_DoubleEndedQueue.print_structure()

print("--------- POP RIGHT --------")
my_DoubleEndedQueue.pop_right()
my_DoubleEndedQueue.print_structure()

