# DATA-STRUCTURES-AND-ALGORITHMS
* [Linked List](#linked-list)
   * [Linked List 程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/leet%20code/707.%20Design%20Linked%20List.py)
   * [Array比較](#array比較)
* [Stack & Queue](#stack--queue)
   * [Stack 程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/leet%20code/155.%20Min%20Stack.py)
* [Insertion Sort](#insertion-sort)
* [Quick Sort](#quick-sort)
   * [Quick Sort 程式碼](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW_Quick%20Sort/Quick%20Sort.ipynb)
   * [過程](#過程)
   * [過程(另外存取空間)](#過程另外存取空間)
* [Heap Sort](#heap-sort)

## Linked list
**連結串列**，使用node(節點)來記錄、表示、儲存資料，並利用pointer指向下一個node，以達到node之間的串接，並以NULL為終點。\
將node串接起來後，每一個node裡面都有紀錄下一個node的位子，因此我們可以進行**新增節點、刪除節點、走訪節點及取得節點內的資料**等操作。\
但是若我們要擷取的資料不是在第一個node的話，就必須從第一個開始走訪到我們要找的位置，所以需要***花費較長的時間與較大的記憶體處理***。
[Linked List 程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/leet%20code/707.%20Design%20Linked%20List.py)
<br>
<br>

![](https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/LinkedList/Intro/f2.png?raw=true)
[圖面來源](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)
<br>
<br>

### Array比較
優點：
  * 可直接使用index
  * 較節省記憶體，不需要pointer來處理資料，
  * ***與Linked List相比較有效率***
  
缺點：
  * 新增刪除很麻煩
  * 只要移動一個，就全部都要移動
  
適合使用時機：
  * 要快速存取資料
  * 已知矩陣大小、資料數量
  * 記憶體空間要求小

## Stack & Queue
[Stack 程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/leet%20code/155.%20Min%20Stack.py)
## Insertion Sort


## Quick Sort
**快速排序法**，先決定取一個固定的位子為pivot，再依序將其餘的數值與pivot比大小，將比pivot小的都丟掉左邊，比pivot大的都丟到右邊。 再來將比pivot小的那些數值再比一次大小，並一樣取第一個為pivot，比pivot大的也用同樣的方式處理，直到不能再處理，亦即所有數值都依照大小都排好了。
[Quick Sort 程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW1/Quick_Sort_05113009.py)

### 過程
['54',26,93,17,77,31,44,55,20] --> list[left]=93, list[right]=20 --> 交換位置變成['54',26,20,17,77,31,44,55,93] --> list[left]=77, list[right]=44 -->交換位置變成['54',26,20,17,44,31,77,55,93] --> list[left]=77, list[right]=31 --> right < left --> pivot與list[right]交換值 --> [31,26,20,17,44,'54' ,77,55,93] 

-->第一次排序完成，接著再將小於54的數列依照此法排序，大於54的數列也是如此，最後就會得出依照大小排序好的 [17, 20, 26, 31, 44, 54, 55, 77, 93]

![](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW_Quick%20Sort/Quick%20Sort%20Demo.jpg)

### 過程(另外存取空間)
>['54',26,93,17,77,31,44,55,20] --> small=[26,17,31,44,20] , big=[93,77,55] , pivotlist=[54] 
>>['26',17,31,44,20] --> small=[17,20] , big=[31,44] , pivotlist=[26] --> return small + pivotlist + big --> [17,20,26,31,44] 
>>['93',77,55] --> small=[77,55] , big=[] , pivotlist=[93] <br/>
>>>['77',55] --> small=[55] , big=[] , pivotlist=[77] --> [55,77]
>>>>[55,77,93]

return small + pivotlist + big --> [17, 20, 26, 31, 44, 54, 55, 77, 93]
<br>
<br>

## Heap Sort
### ***以陣列的形式表現，但要以二元樹的方式理解。***
每個子結點都必須小於父節點，當子結點大於父結點時，兩者交換位置，直到所有子結點都小於父結點，並且在最後將第一個結點拿出來，再將最後一個結點移到最前面，繼續進行排序，直到排序結束。<br>

![](https://algorithm.yuanbin.me/shared-files/images/Heapsort-example.gif)
[圖片來源](https://algorithm.yuanbin.me/zh-tw/basics_data_structure/heap.html)

  * python index:i
    * left:2i+1
    * right:2i+2
    
    
    
## Merge Sort


## Binary Tree




