# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        
class Solution(object):
    def insert(self, root, val):
        if root == None:
            root = TreeNode(val)
        else:
            if val <= root.val:
                if root.left == None:
                    root.left = TreeNode(val)
                    temp = root.left
                else:
                    temp = self.insert(root.left,val)               
                
            if val > root.val:
                if root.right == None:
                    root.right = TreeNode(val)
                    temp = root.right
                else:
                    temp = self.insert(root.right,val)
        return temp
                
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        
    def delete(self,root,target):
        global temp2
        temp2 = []
        self.makelist(root,temp2)

        if root == None:
            return
        else:
            if root.val == target:
                if root.left == None and root.right == None:
                    root=None
                    return
                if root.right:
                    nroot = self.minnode(root.right)
                else:
                    if root.left:
                        nroot = self.maxnode(root.left)
                temp2.remove(nroot.val)
                root.val = nroot.val


            root.left = None
            root.right = None
            for i in temp2[1:]:
                if i != target:
                    self.insert(root,i)
        return root
                    
        """ 
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        
    def search(self, root, target):
        if root == None:
            return None
        if root.val == target:
            return root
        else:
            if target > root.val:
                temp = self.search(root.right,target)
            else:
                temp = self.search(root.left,target)
                
        return temp
                
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        
    def modify(self, root, target, new_val):
        a = self.height(root)
        if root == None:
            return
        else:
            global temp4
            global temp3
            temp3 = []
            temp4 = []
            self.makelist(root,temp3)
            if root.val == target:
                root.val = target
                temp[0] = target
                if root.left==None and root.right == None:
                    return
            root.left,root.right = None,None
            temp4.append(root.val)
            for i in temp3[1:]:
                if i == target:
                    i = new_val
                temp4.append(i)
                self.insert(root,i)
                
            if self.height(root) > a:  #reconstruction tree
                b = sorted(temp4)
                nroot = b[len(b)//2-1]
                root.val = nroot
                root.left,root.right = None,None
                temp4.remove(nroot)
                for i in temp4:
                    if i == target:
                        i = new_val
                    self.insert(root,i)  
        return root
        
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
                        
    def makelist(self,root,temp): 
        temp.append(root.val)
        if root.left:
            self.makelist(root.left,temp)
        if root.right:
            self.makelist(root.right,temp)
            
    def maxnode(self,root): 
        if root == None:
            return
        while root.right != None:
            root = root.right
        return root
        
    def minnode(self,root): 
        if root == None:
            return
        while root.left != None:
            root = root.left
        return root
            
    def height(self,root):  
        if root is None: 
            return 0 
        else :
            leftheight = self.height(root.left)
            rightheight = self.height(root.right)
            
            if leftheight>rightheight:
                return leftheight + 1
            else:
                return rightheight +1


#https://www.itread01.com/content/1542339850.html ---> delete 
#https://github.com/pecu/DSA/blob/master/10_RedBlackTree/RBT.py ---> preorder
#https://www.itread01.com/content/1542339850.html ---> maxnode & minnode
#https://www.geeksforgeeks.org/level-order-tree-traversal/ ---> height            
