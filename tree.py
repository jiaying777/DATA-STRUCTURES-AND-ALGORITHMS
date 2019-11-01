class Tree:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.parent = None
        self.size = None
    
    def add_root(self,val):
        self.val = val
        self.size += 1
        
            
    def add_left(self,val,index):
        if self.val == None:
            self.val = val
        
        if self.left == None:
            self.left.val = val
            
        else:    
            replace(val,index)
            
        self.size += 1
        self.left.parent = self
            
    def add_right(self,val,index):
        if self.val == None:
            self.val = val
        
        if self.left == None:
            self.left.val = val
            
        else:    
            replace(val,index)
        
        self.size += 1
        self.right.parent = self

    def replace(self,val,index):
        
            
