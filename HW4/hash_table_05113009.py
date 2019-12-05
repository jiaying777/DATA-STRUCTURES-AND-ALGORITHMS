class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key):
        temp = self.MD5(key)
        temp = int(temp,16)
        index = temp % self.capacity
        if self.data[index] == None:
            self.data[index] = ListNode(temp)
            return
        else:
            node = self.data[index]
            while node:
                if node.val == temp:
                    return
                if node.next == None:
                    node.next = ListNode(temp)
                    return
                node = node.next

                  

    def remove(self, key):
        temp = self.MD5(key)
        temp = int(temp,16)
        index = temp % self.capacity
        node = self.data[index]
        prenode = node 
        
        if node:
            if node.val == temp:
                if node.next:
                    self.data[index] = node.next
                    return
                else:
                    self.data[index] = None
                    return
        
        while node:
            if node.val == temp:
                if node.next:
                    prenode.next = node.next
                    return
                else:
                    prenode.next = None
                    return
            prenode = node
            node = node.next        

        

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
        
        

    def MD5(self, key):
        from Crypto.Hash import MD5
        a = MD5.new(key.encode('utf-8'))
        return a.hexdigest()
    


#https://www.youtube.com/watch?v=oqzStHk36PI&feature=youtu.be 程式碼參考
#https://blog.kdchang.cc/2017/08/15/learning-programming-and-coding-with-python-list-tuple-dict-set/ 觀念參考
#https://www.itread01.com/content/1542966064.html 觀念參考
#http://codepad.org/NxRlGE3H 程式碼格式範例
