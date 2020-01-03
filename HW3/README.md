# Binary Search Tree
## insert
insert(root,val)\
新增功能是將一個新的值(val) 放入BST 裡面，每個值都有一個自己的TreeNode，所以我們需要新增一個含有val 的TreeNode ，並且放入BST裡。<br>
根據BST的規則，左邊放入比自己小的，右邊放比自己大的，一樣大的值也放入左邊(自己設的) 所以我們將要新增的TreeNode(val) 必須根據此規則找到空的位置放入。<br>
例如：<br>
有一棵樹的值為[6,3,7,3,8,4,9,1]，要新增''4''這個值<br>
樹：

                    6
                   /  \
                 3     7
                / \     \
              3    4     8 
             /             \
            1                9
            
新增"4"：

                    6
                   /  \
                 3     7
                / \     \
              3    4     8 
             /    /        \
            1   '4'          9
            
因為 4<6(root) 所以往左邊， 4>3(root.left) 往右，4=4(root.left.right) 往左，所以會放在第三層的4左邊，因此新增的TreeNode(4)位置為：root.left.right.left<br>

所以根據這個邏輯，我的程式碼運作為：如果沒有root，那麼root = TreeNode(val)，如果 val>root.val 則往右，val<=root.val 則往左。<br>

    if val>root.val:
        root.right = TreeNode(val)
    if val<=root.val:
        root.left = TreeNode(val)
        
但是我們必須先判斷root是否有children，如果有我們就要往下一層尋找空的位置，所以需要增加條件：<br>

    if val>root.val:
        if root.right == None:
            root.right = TreeNode(val)
        else:
            insert(root.right,val)
            
    if val<=root.val:
        if root.left == None:
            root.left = TreeNode(val)
        else:
            insert(root.left,val)
            
使用遞迴 insert(root,val) 再進行下一層的搜索，直到找到適當的位置後，放入新增的TreeNode(val)         


