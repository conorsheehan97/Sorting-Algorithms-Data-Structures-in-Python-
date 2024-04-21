
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.Head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Instantiating a Node
        new_node.next = self.Head  # New node must point at previous head if its at start
        self.Head = new_node  # The Linked List Object has a new head

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.Head:  # If the list is empty, i.e. Head == None
            self.Head = new_node  # The Head = New Node
            return
        last_node = self.Head  # Think of this as a temporary value
        while last_node.next:  # Here we recursively assign last node to the next node, while nodes had a next attribute
            last_node = last_node.next
        last_node.next = new_node  # Once this loop ends, the last remaining node's next attribute is assigned to the new 'last node'

    def insert_after_node(self, data, node):
        new_node = Node(data)
        if not node:  # if the previous node is not in the linked list, return a message
            print('Node not in list')
            return
        prev_node = node  # just for clarity on my end
        # the order is important here, we must copy the previous nodes 'next' attribute
        # to new node, before we repoint it at the inserted node
        new_node.next = prev_node.next
        prev_node.next = new_node

    def display(self):
        current = self.Head  # Starting at the Head of the Linked List
        while current:  # While we're in the list, and not past the tail
            print(current.data, end = ' -> ')  # print the data, point to the next element
            current = current.next  # iterate
        print('None')  # Show we've reached our final destination

    def length(self):
        count = 0  # declaring a counter for the length
        current = self.Head  # starting from the head
        while current:  # while current != False (or None)
            count += 1  # increment our count
            current = current.next  # moving down our linked list
        return count

    def is_empty(self):
        if not self.Head:  # If we've no head, it means we're empty, return True
            return 1
        else:
            return 0  # Else we return False

