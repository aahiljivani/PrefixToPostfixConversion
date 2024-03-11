class stack:
    """
    A simple implementation of a stack data structure.

    Attributes:
        items (list): A list that will contain the stack elements.

    Methods:
        is_empty(self):
            Checks if the stack is empty. Returns True if it is, False otherwise.

        peek(self):
            Returns the top element of the stack without removing it. If the stack is empty,
            this method will return None.

        push(self, element):
            Adds an element to the top of the stack.

        pop(self):
            Removes and returns the top element of the stack. If the stack is empty,
            it returns None instead of raising an exception.

        GetLength(self):
            Returns the number of elements in the stack.

    This stack class provides the operations to implement the Stack ADT
    where you may add or remove items from the top of the stack only.
    We have assumed here that stacks are not iterable, and cannot be indexed.
    """

    def __init__(self):
        # Initializes a new empty stack.
        self.items = []

    def is_empty(self):
        # Returns True if the stack is empty, False otherwise.
        return len(self.items) == 0

    def peek(self):
        # Returns the top element of the stack without removing it.
        if not self.is_empty():
            return self.items[-1]
        return None

    def push(self, element):
        # Adds an element to the top of the stack.
        self.items.append(element)

    def pop(self):
        # Removes and returns the top element of the stack. Returns None if the stack is empty.
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def GetLength(self):
        # Returns the number of elements in the stack.
        return len(self.items)
