import tarfile


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__ (self, value):
        new_node = Node(value)

        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.value)
            actual_node = actual_node.next


    def append(self, value):

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # pyright: ignore[reportAttributeAccessIssue, reportOptionalMemberAccess]
            self.tail = new_node

        self.length +=1



    def pop_intro(self):
        if self.length == 0:
            return

        if self.length == 1:
            self.head = None
            self.tail = None
            return

        previous_node = self.head
        next_node = self.head
        print(next_node)

        before_last = False
        #while not before_last:
        #    if next_node == None:


            
        

    def pop_first(self):
        ...

    def get(self, value):
        ...

    def set(self, value):
        ...

    def insert(self, value):
        ...
    
    def remove(self, value):
        ...

    def reverse(self):
        ...
        

ll = LinkedList(10)
ll.append(30)
ll.append(40)
ll.append(50)

ll.pop_intro()

ll.print_list()