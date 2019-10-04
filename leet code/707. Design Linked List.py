class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
     
        if self.val == None:
            return -1
        if index == 0:
            return self.val
        
        i = 1
        if self.next != None:
            while index == i:
                return self.next.val
                self.next = self.next.next
                i += 1
        else:
            return -1
        
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val == None:    
            self.val = val
            return
            
            
        a = self.val
        b = self.next
        self.val = val
        
        self.next = MyLinkedList()
        self.next.val = a
        self.next.next = b
        
        return
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val == None:
            self.val = val
            return
            
        c = self
        while self.next != None:
            c = self.next
        c.next = MyLinkedList()
        c.next.val = val
        return
