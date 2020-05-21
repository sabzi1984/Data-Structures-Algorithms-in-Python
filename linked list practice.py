class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position<1:
            return None
        elif position >=1:
            i=1
            current=self.head
            while current and i<=position:
                if i==position:
                    return current
                i+=1
                current=current.next
            return None
       
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position>1:
            i=1
            current=self.head
            while current and i<=position:
                i+=1
                current=current.next
                if i==position-1:
                    new_element.next=current.next
                    current.next=new_element    
        elif position==1:
            new_element.next=self.head
            self.head=new_element
            
        pass
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current=self.head
        if current.value==value:
            self.head=self.head.next
            current.next=None
            
        else:
            before=None
            while current.next:
                if current.value==value:
                    before.next=current.next
                before=current
                current=current.next                                  
            return None
        pass

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print (ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)