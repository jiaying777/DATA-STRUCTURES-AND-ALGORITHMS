# BFS & DFS
[程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW5/BFS_05113009.py)<br>
[學習歷程](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW5/BFS%26DFS_流程圖、學習歷程與原理與比較.ipynb)<br>

**BFS(Breadth-First Search, 廣度/橫向優先搜尋)：<br>**
為廣義的Level-Order Traversal，將使用情境從Tree推廣至Graph，先走訪所有相鄰的節點，再以剛剛走訪的節點當作下一次搜尋的起點，搜尋相鄰的所有節點，逐一走訪，直至所有節點都走訪為止。以Tree來說明，就是將同一深度(level)的所有節點都走訪完才會進到下一個深度，直到所有節點都被尋訪過。<br>
BFS屬於盲目搜索(uninformed search)是利用佇列(Queue)來處理，確保先被走訪到的節點會優先成為新的搜尋起點(先進先出)。

<br>

**DFS(Depth-First Search, 深度/縱向優先搜尋)：**<br>
是從某一節點出發後，遇到還未走訪的相鄰節點則走訪，直到沒有未走訪的相鄰節點可搜尋，則退回前一個節點尋找是否有還未走訪的節點，直至所有節點都被走訪為止。 <br>
DFS屬於盲目搜索(uninformed search)是利用堆疊(Stack)來處理，確保先遇到的鄰點就先走訪(後進先出)。

<br>

**BFS v.s. DFS**<br>
* 時間複雜度皆為：O(V+E) ---- *(Ｖ為圖的頂點數，E為邊數 )*
* 記憶體空間：BFS > DFS
* BFS是利用Queue(先進先出)處理，DFS則是用Stack(後進先出)處理。
* BFS同深度搜尋完才會往下一層搜尋，DFS先遇到的鄰點就先訪問並以其作為新的搜尋起點。

<br>
## 流程圖
<img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/圖/bfs.png" width="70%"> 
<img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/圖/dfs.png" width="70%"> 
