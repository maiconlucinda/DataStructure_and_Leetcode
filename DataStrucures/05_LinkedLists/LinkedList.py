


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
        return True


    # Removing the last item
    def pop(self):
        if self.length == 0:
            return

        if self.length == 1:
            return_value = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return return_value

        previous_node = self.head
        actual_node = self.head

        while actual_node is not self.tail:
            previous_node = actual_node
            actual_node = actual_node.next
        
        previous_node.next = None
        self.tail = previous_node
        self.length -= 1
        return actual_node


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

            
    def pop_first(self):
        if self.length == 0:
            return
        
        if self.length == 1:
            to_return = self.head
            self.head = None
            self.tail = None

            self.length = 0
            return to_return


        to_return = self.head
        self.head = self.head.next
        to_return.next = None
        self.length -= 1
        if self.length == 0:
            sail.tail = None
        return to_return



    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        actual_node = self.head
        for _ in range(index):
            actual_node = actual_node.next

        # Return object node
        return actual_node


    # Change a certain value
    def set_value(self, index, value):
        node_to_change = self.get(index)

        if node_to_change:
            node_to_change.value = value
            return True
        else:
            return False


    # Insere um valor em um certo Index
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False

        elif index == 0:
            return self.prepend(value)
        
        elif index == self.length:
            return self.append(value)

        else:
            new_node = Node(value)
            node_before = self.get(index -1)

            new_node.next = node_before.next
            node_before.next = new_node
            self.length += 1
            return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return False

        if index == 0:
           return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        previous_node = self.get(index -1)
        actual_node = previous_node.next

        previous_node.next = actual_node.next
        actual_node.next = None
        self.length -= 1
        return actual_node


    def reverse(self):
        previous_node = None
        actual_node = self.head

        while actual_node is not None:
            next_node = actual_node.next
            actual_node.next = previous_node
            previous_node = actual_node
            actual_node = next_node

        self.head, self.tail = self.tail, self.head



ll = LinkedList(10)
ll.append(30)
ll.append(40)
ll.append(50)
#print(ll.get(2))

ll.set_value(2, 80)
ll.insert(2, 70)
ll.remove(2)
ll.reverse()
ll.print_list()