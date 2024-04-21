class Stack:
    def __init__(self):  # Using the Dunder __init__ constructor to give each instance a list
        self.stack = []

    def push(self, item):
        self.stack.append(item)  # Here we add the item at the end of the list
        # This is important, as it must be at the end, to work in conjunction with
        # The pop() method to fulfill the LIFO principle of Stacks

    def is_empty(self):
        if len(self.stack) == 0:
            return True  # Simply evaluates to True if the Stack is empty

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()  # If we're not empty, using the pop method remove the top element
        else:  # Pop removes the list item at the last index
            print('Stack is presently empty')

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]  # If the stack isn't empty, give us a sconce inside
        else:
            print('Nothing to show, Stack is empty!')

    def size_stack(self):  # returns the size of the stack using the length function
        return len(self.stack)

