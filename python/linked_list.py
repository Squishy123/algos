class LinkedList():
    def __init__(self, data=None, head=None, tail=None):
        self.data=data
        self.head=head
        self.tail=tail

    # Returns the last element of the linked list
    def peek(self):
        if(self.tail == None):
            return self.data
        else:
            return self.tail.peek()

    # Returns and removes the last element of the linked list
    def pop(self):
        if(self.tail == None):
            data=self.data
            self.head.tail=None
            self.head=None
            return data
        else:
            return self.tail.pop()            

    # Returns the first element of the linked list
    def peekFirst(self):
        if self.head == None:
            return self.data
        else:
            return self.head.peekFirst()

    # Returns and removes the first element of the linked list
    def dequeue(self):
        if self.head == None:
            data=self.data            
            self.tail.head=None
            self.__dict__.update(self.tail.__dict__)
            return data
        else:
            return self.head.dequeue()

    # Appends data to the tail of the linked list
    def push(self, data):
        if self.data == None:
            self.data=data
        elif self.tail == None:
            self.tail=LinkedList(data, self)
        else:
            return self.tail.push(data)

    # Appends data to the head of the linked list
    def unshift(self, data):
        if self.head == None:
            self.head=LinkedList(data, self, None, self)
        else:
            return self.head.unshift(data)

    # Return a string representation of the linked list
    def toString(self):
        if self.tail == None:
            return self.data
        else: 
            return str(self.data) + '\n' + str(self.tail.toString())

ll=LinkedList()
for i in range(10):
    ll.push(i)

#print(ll.toString())
#print(ll.dequeue())
#print(ll.dequeue())
ll.dequeue()
ll.dequeue()
print(ll.pop())
print(ll.toString())