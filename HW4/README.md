# Hash Table
[程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW4/hash_table_05113009.py)<br>
[學習歷程](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW4/hash%20table%20學習歷程、流程圖與文字說明.ipynb)<br>

* Hash Function 是將輸入的值轉譯成另外的值，特性為快速、單向性、不可逆性，只有輸入的值能得到輸出的值，輸出的值無法反向得到輸入的值。且好的Hash Function 不易出現碰撞，所以當出現碰撞卻沒抑制的話，會使資料更難查詢。<br>
* Hash Table 是一種儲存(key,value)的資料結構，一個key對應一個value，key可以想像成標籤，要找到這筆value就必須要有key才找得到。Table size 若是太小會使資料太過集中，導致查詢效率降低，因此Table size的設定就非常重要。<br>
* Hash 時間複雜度： O(1)     <      ( *array: O(n), binary search tree: O(logn)~O(n)* )<br>
* Chaining概念：可能有不同的資料分配到同一組，所以用linked list將其都串在一起，可以解決碰撞問題。

在Hash Function設計不良的狀況下，有可能會都分到同一組，導致連接很長的linked list，這樣就失去Hash的優勢了，並且可能會發生碰撞，所以為了減少這種狀況的發生，可以使用Cryptographic Hash Function，利用加密的方式來避免碰撞的發生，所以一般都會使用Cryptographic Hash Function的方法，Cryptographic Hash Function有很多不同的演算法，其中包含常見的MD5、SHA等，除此之外，還可以提高Table size，使資料分佈的更分散且平均，以減少碰撞發生。



Hash常用於：搜尋引擎、檔案校對碼、使用者密碼儲存比對。<br>
只需要將使用者輸入的密碼hash過後再進行比對，也可以將不公開的密碼加密後存入Hash Table裡，這樣既可以比對密碼是否正確，也可防止密碼外洩的可能性。<br>
Hash功能：新增、刪除、查詢



<img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/圖/hash_add.png" width="70%"> 
<img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/圖/hash_contains.png" width="70%"> 
<img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/圖/hash_remove.png" width="70%"> 
