class Tree:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.parent = None
             
    def add_root(self,val):
        self.val = val
    
    def add_left(self,val):
        if self.val == None:
            self.val = val
        
        if self.left == None:
            self.left.val = val
        else:    
            replace(val)
            
    def add_right(self,val):
        if self.val == None:
            self.val = val
            return
        
        if self.left == None:
            self.left.val = val
            
        else:    
            replace(val)
            
