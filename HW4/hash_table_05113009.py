class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, key):
        temp = self.MD5(key)
        temp = int(temp,16)
        index = temp % self.capacity
        if self.data[index] == None:
            self.data[index] = ListNode(temp)
        else:
            node = self.data[index]
            while node:
                if node.val == temp:
                    return
                if node.next == None:
                    node.next = ListNode(temp)
                    return
                node = node.next

                  
        """
        :type key: str
        :rtype: None
        """
    def remove(self, key):
        temp = self.MD5(key)
        temp = int(temp,16)
        index = temp % self.capacity
        
        if self.data[index].val == temp:
            if self.data[index].next:
                self.data[index] = self.data[index].next
            else:
                self.data[index] = None
        else:
            node = self.data[index]
            while node.next:
                if node.next.val == temp:
                    if node.next.next:
                        node.next = node.next.next
                        return
                    else:
                        node.next = None
                        return
                if node.next.next:
                    node = node.next

        
        """
        :type key: str
        :rtype: None
        """
    def contains(self, key):
        temp = self.MD5(key)
        temp = int(temp,16)
        index = temp % self.capacity
        node = self.data[index]

        while node:
            if node.val == temp:
                return True
            node = node.next
        return False       
        
        
        """
        :type key: str
        :rtype: bool(True or False)
        """
    def MD5(self, key):
        from Crypto.Hash import MD5
        a = MD5.new(key.encode('utf-8'))
        return a.hexdigest()
    


