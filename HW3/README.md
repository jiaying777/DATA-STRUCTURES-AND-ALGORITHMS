# Binary Search Tree
BST為二元樹，亦即每一個節點底下都只能有兩個子節點，BST與Binary Tree最大的差別在於有大小順序，Binary Tree每一個節點底下最多只能有兩個子節點，這點與BST一樣，不過Binary Tree的任意子節點可以大於、等於或小於父節點，但BST不行，BST需要透過比較大小進行搜尋排序等等動作，也正是因為有這項特徵，所以方便我們尋找資料，不需要走訪過每一個節點。
<br>
Binary Search Tree:
* 每個節點底下最多只會有兩個子節點
* 需比較大小，非數值型資料，則可以新增編號等等，以便排序
* 有一定的排序規則：
        - 比節點小的放左邊
        - 比節點大的放右邊
        - 與節點相等的可放左或右邊，不過要統一（自行定義
<br>

* [功能說明](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW3/binary%20search%20tree%20功能說明.ipynb)
* [程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW3/binary_search_tree_05113009.py)
* [學習歷程](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW3/binary%20search%20tree%20學習歷程與流程圖.ipynb)
<br>

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
<br>
        
## delete
delete(root,target)\
刪除功能是將樹中原有的值刪除，亦即將整個TreeNode(val)刪除，由於刪除其中的TreeNode可能會破壞BST原本的結構與規則，所以我們需要在移動最小結構的狀況下執行。此刪除功能是將所有擁有相同的值的TreeNode都刪除。<br>
例如：<br>


                    6
                   /  \
                 3     7
                / \     \
              3    4     8 
             /             \
            1                9
            
刪除數值為3的TreeNode，有2個TreeNode的值為3，所以需要都刪除：<br>


                    6
                   /  \
                 1     7
                  \      \
                   4      8 
                            \
                             9
                                        
搜尋方式為 3!=6 and 3<6，所以往左，3==3 刪除，因為找到target了，但是有可能有相同的值，根據[insert](#insert)相同的值會放在左邊，所以往左繼續找找看還有沒有含有3的TreeNode，3!=-5 and 3>1，往右但是此處的TreeNode(1)沒有children，則停止搜尋。

如果刪除的TreeNode(val)底下有children ，則刪除的TreeNode會用其底下的TreeNode 來作替代，規則為：<br>
若左邊有children，則找左邊children中值最大的TreeNode來取代，若是左邊沒有則判斷右邊是否有children，如果有則找出右邊值最小的TreeNode來取代。<br>
<br>

## search
search(root,target)\
搜尋功能是從BST中找出值符合目標的TreeNode，並將其回傳。<br>
此功能只能回傳離root最近且含有target的TreeNode，所以並不會將所有含target的TreeNode都回傳。<br>
例如：<br>

                6
               /  \
             3     7
            / \     \
          3    4     8 
         /             \
        1                9
        
搜尋target = 7：

                6
               /  \
             3    '7'
            / \     \
          3    4     8 
         /             \
        1                9
        
        
則會回傳含有7的TreeNode，位置為：root.left<br>
<br>

## modify
modify(root,target,new_val)\
修改功能是更改BST裡面現有TreeNode的值，由於修改TreeNode的值，所以可能會違反BST的規則，因此需要重建BST。<br>

                6
               /  \
             3     7
            / \     \
          3    4     8 
         /             \
        1                9
        
修改3為9：

                6
               /  \
             9     7
            / \     \
          9    4     8 
         /             \
        1                9
        
搜尋方式：3!=6 and 3<6 往左，３==3 修改為9，與target相符往左找找看還有沒有相同的值，３==3 修改為9，繼續往左找，3!=1 and 3>1 往右，沒有children了，所以結束搜尋修改。<br>
修改完的BST並不符合規則，所以我們要進行重建的動作。

                6
               /  \
             1     9
              \     \
               4     9 
                       \
                        7
                          \
                           8
                             \
                              9
                              
重建完的BST的深度比原本還要深且變成linked list，這樣就失去BST的好處了，所以我們需要對BST在進行一次重建。<br>


