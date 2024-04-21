class Queue:
    def __init__(self):
        self.queue = []  # Constructor Method to initialize instances

    def enqueue(self, item):  # Adding elements to Queue method
        self.queue.append(item)

    def dequeue(self):  # Removing elements from Queue method
        if len(self.queue) != 0:
            return self.queue.pop()
        else:
            print('The queue is empty, what the frick?')

    def peek(self):  # Method to have a sconce at the First element added to Queue
        if len(self.queue) > 0:
            return self.queue[0]

        else:
            print('Nothing to peek at')


    def size(self):  # Method to get the size of the Queue
        if len(self.queue) > 0:
            return(len(self.queue))

        else:
            return None

    def is_empty(self):  # Method to check if the Queue is empty
        return len(self.queue) == 0
