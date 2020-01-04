# Kruskal & Dijkstra  
[程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW6/Dijkstra_05113009.py)\
[學習歷程](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW6/Dijkstra%20%26%20Kruskal%20學習歷程與文字說明.ipynb)

## Kruskal

Kruskal演算法是一種用來尋找無向圖中最小生成樹（Minimum Spanning Tree）的演算法，亦即找出圖中邊權重最小的樹，且每個點都要包含在其中，但不需要考慮root應該為哪個點、樹是否有平衡或是樹高大小等等，只需要找出最小權重總和的樹即可。用來解決同樣問題的還有前面Prim演算法和Boruvka演算法等，和Boruvka演算法不同的地方是，Kruskal演算法在圖中存在相同權重的邊時也有效。

    1. 先把每個節點都當成一棵樹
    2. 再來排序所有邊的權重，由小到大（最小生成樹）
    3. 若兩節點分別為不同的樹，此條邊則為MST的邊
    4. 反之若為同一顆樹，連結此邊會產生loop，因此應該捨去這條邊    
    
    *** 可能不只有一個解，只要權重為最小即可
    時間複雜度：O(ElogE)或者O(ElogV)

## Dijkstra

Dijkstra演算法為指定一個點到其他點的最短路徑（單源最短路徑），最簡單的執行方法就是將每個節點在不經過其他節點的情況下，到其他節點的權重(weight/cost)儲存在串列或陣列裡，因此有幾個節點就需要進行多少次搜尋，時間複雜度為O(V²)。

<br>

    1. 先將所有節點到其他節點（不經過其他節點）的權重存到串列或陣列中，若是無法到達則紀錄∞
    2. 選定起點(a)，將(a)能到達的點之權重先加入最短路徑中，並找出串列或陣列中距離最近的點(b)，並確定為最短路徑
    3. 從(a)->(b)->？，將(b)能走到的點之權重加入（a->b->c的權重總和），若為已尋訪過的節點則判斷（a->b->c）是否小於（a->c），如果小於
        則更新最短路徑的權重，最後再找出未確定節點中距離最近的點。
    4. 重複執行步驟3，直到全部都確定為起點到任一點的最短路徑為止。
    
    時間複雜度：O(V²)   V:節點個數
    
    
# 流程圖
<img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/圖/Kruskal.png" width="70%"> 
<img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/圖/Dijkstra.png" width="70%">
 
