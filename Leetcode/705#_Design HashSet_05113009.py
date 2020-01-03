class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyHashSet:

    def __init__(self,capacity=1000):
        self.capacity = capacity
        self.data = [None]*capacity
        """
        Initialize your data structure here.
        """
        

    def add(self, key: int) -> None:
        temp = key % self.capacity
        if self.data[temp] == None:
            self.data[temp] = ListNode(key)
            return
        else:
            node = self.data[temp]
            while node:
                if node.val == key:
                    return
                prenode = node
                node = node.next
                
            newnode = ListNode(key)
            prenode.next = newnode

            

    def remove(self, key: int) -> None:
        temp = key % self.capacity
        node = self.data[temp]
        prenode = node 
        if node:
            if node.val == key:
                if node.next:
                    self.data[temp] = node.next
                    return
                else:
                    self.data[temp] = None
                    return
        
        while node:
            if node.val == key:
                if node.next:
                    prenode.next = node.next
                    return
                else:
                    prenode.next = None
                    return
            prenode = node
            node = node.next        
        
        if node == None:
            return
        
        

    def contains(self, key: int) -> bool:
        temp = key % self.capacity
        node = self.data[temp]
        while node:
            if node.val == key:
                return True
            node = node.next
        return False
        """
        Returns true if this set contains the specified element
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
