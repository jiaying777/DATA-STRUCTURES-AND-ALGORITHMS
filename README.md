# DATA-STRUCTURES-AND-ALGORITHMS
* [Week1](#Week1)
* [Week2](#Week2)
  * [Linked List](#linked-list)
     * [課堂投影片](https://docs.google.com/presentation/d/e/2PACX-1vTB218-EdUZ5jpNz6Uv4TOZQc37Y281v128_aRcWC6EhkTQs5bS8fh7yysmcuzb9R2QPN6_PDshFWL_/pub?start=false&loop=false&delayms=3000&slide=id.p)
     * [Linked List 程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/class/01_LeetCode_707.%20Design%20Linked%20List.py)
     * [Array比較](#array比較)
* [Week3](#Week3)
  * [Stack & Queue](#stack--queue)
     * [課堂投影片](https://docs.google.com/presentation/d/e/2PACX-1vQ1hb79im0vqpApCttGnXAFRT8SqH9HQP0b_oyVRCV8SVyiHLkHJjidYGAfxkvq468QMumFIDdTeiB-/pub?start=false&loop=false&delayms=3000&slide=id.p)
     * [Stack程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/class/02_LeetCode_155.%20Min%20Stack.py)
     * [Queue程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/class/02_LeeCode_232.%20Implement%20Queue%20using%20Stacks.py)
* [Week4](#Week4)
  * [Insertion Sort](#insertion-sort)
* [Week5](#Week5)
  * [Quick Sort](#quick-sort)
     * [Quick Sort 程式碼](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW_Quick%20Sort/Quick%20Sort.ipynb)
     * [學習歷程](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW1/Quick%20Sort%20程式碼與學習歷程.ipynb)<br>
     * [過程](#過程)
     * [過程(另外存取空間)](#過程另外存取空間)
* [Week6](#Week6)
  * [Heap Sort](#heap-sort)
     * []()

# Week1
課程介紹

# Week2
[課堂投影片](https://docs.google.com/presentation/d/e/2PACX-1vTB218-EdUZ5jpNz6Uv4TOZQc37Y281v128_aRcWC6EhkTQs5bS8fh7yysmcuzb9R2QPN6_PDshFWL_/pub?start=false&loop=false&delayms=3000&slide=id.p)

## Linked list
**連結串列**，使用node(節點)來記錄、表示、儲存資料，並利用pointer指向下一個node，以達到node之間的串接，並以NULL為終點。\
將node串接起來後，每一個node裡面都有紀錄下一個node的位子，因此我們可以進行**新增節點、刪除節點、走訪節點及取得節點內的資料**等操作。\
但是若我們要擷取的資料不是在第一個node的話，就必須從第一個開始走訪到我們要找的位置，所以需要***花費較長的時間與較大的記憶體處理***。
[Linked List 程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/class/01_LeetCode_707.%20Design%20Linked%20List.py)
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

# Week3
## Stack & Queue
[課堂投影片](https://docs.google.com/presentation/d/e/2PACX-1vQ1hb79im0vqpApCttGnXAFRT8SqH9HQP0b_oyVRCV8SVyiHLkHJjidYGAfxkvq468QMumFIDdTeiB-/pub?start=false&loop=false&delayms=3000&slide=id.p)\
[Stack程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/class/02_LeetCode_155.%20Min%20Stack.py)\
[Queue程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/class/02_LeeCode_232.%20Implement%20Queue%20using%20Stacks.py)\

### Stack
Stack（堆疊）為一種資料結構，可以用 Array 或是 Linked List 的形式來操作，Stack的特性為「先進後出，後進先出」，就如同籃子一樣，越晚放進去的東西會放在越上面，所以上面的東西得先拿出來，最下面的東西才有可能拿出來。<br>

#### Stack 功能：<br>
* Push(data)：把資料放進Stack。
* Pop：把「最上面」的資料從Stack中移除。
* Top：回傳「最上面」的資料，不影響資料結構本身。
* IsEmpty：確認Stack裡是否有資料，不影響資料結構本身。
* getSize：回傳Stack裡的資料個數，不影響資料結構本身。
<img src="https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/Stack/intro/f1.png?raw=true" >
<br>
[參考資料](http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html)

### Queue
Queue（佇列）為一種資料結構，可以用 Array 或是 Linked List 的形式來操作，Queue的特性為「先進先出，後進後出」，就如同排隊一樣，先來的人就可以先買東西，後來的人就要等前面的人都買完了才可以買。<br>

#### Queue 功能：
* Push(data)：把資料從Queue的「後面」放進Queue，並更新成新的back。
* Pop：把front所指向的資料從Queue中移除，並更新front。
* getFront：回傳front所指向的資料。
* getBack：回傳back所指向的資料。
* IsEmpty：確認Queue裡是否有資料。
* getSize：回傳Queue裡的資料個數。
<img src="https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/Queue/intro/queue.gif?raw=true">
<br>
[參考資料](http://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html)


# Week4
## Insertion Sort




# Week5
## Quick Sort
**快速排序法**，先決定取一個固定的位子為pivot，再依序將其餘的數值與pivot比大小，將比pivot小的都丟掉左邊，比pivot大的都丟到右邊。 再來將比pivot小的那些數值再比一次大小，並一樣取第一個為pivot，比pivot大的也用同樣的方式處理，直到不能再處理，亦即所有數值都依照大小都排好了。\
[Quick Sort 程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW1/Quick_Sort_05113009.py)\
[學習歷程](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW1/Quick%20Sort%20程式碼與學習歷程.ipynb)<br>


時間複雜度  | Quick Sort | Heap Sort | Merge Sort | Insertion Sort | Seletion Sort| 
-------------|------------|-----------|------------|----------------|--------------|
Best Case    | NlogN      |NlogN |NlogN |N|N^2
Average Case | NlogN      |NlogN |NlogN |N^2|N^2
Worst Case   | N^2        |NlogN |NlogN |N^2|N^2



### 過程
['54',26,93,17,77,31,44,55,20] --> list[left]=93, list[right]=20 --> 交換位置變成['54',26,20,17,77,31,44,55,93] --> list[left]=77, list[right]=44 -->交換位置變成['54',26,20,17,44,31,77,55,93] --> list[left]=77, list[right]=31 --> right < left --> pivot與list[right]交換值 --> [31,26,20,17,44,'54' ,77,55,93] 

-->第一次排序完成，接著再將小於54的數列依照此法排序，大於54的數列也是如此，最後就會得出依照大小排序好的 [17, 20, 26, 31, 44, 54, 55, 77, 93]

<img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/圖/Quick%20Sort%20Demo.jpg" width="50%">

### 過程(另外存取空間)
>['54',26,93,17,77,31,44,55,20] --> small=[26,17,31,44,20] , big=[93,77,55] , pivotlist=[54] 
>>['26',17,31,44,20] --> small=[17,20] , big=[31,44] , pivotlist=[26] --> return small + pivotlist + big --> [17,20,26,31,44] 
>>['93',77,55] --> small=[77,55] , big=[] , pivotlist=[93] <br/>
>>>['77',55] --> small=[55] , big=[] , pivotlist=[77] --> [55,77]
>>>>[55,77,93]

return small + pivotlist + big --> [17, 20, 26, 31, 44, 54, 55, 77, 93]
<br>
<br>

# Week6
## Heap Sort
### ***以陣列的形式表現，但要以二元樹的方式理解。***
每個子結點都必須小於父節點，當子結點大於父結點時，兩者交換位置，直到所有子結點都小於父結點，並且在最後將第一個結點拿出來，再將最後一個結點移到最前面，繼續進行排序，直到排序結束。<br>

![](https://algorithm.yuanbin.me/shared-files/images/Heapsort-example.gif)
[圖片來源](https://algorithm.yuanbin.me/zh-tw/basics_data_structure/heap.html)

  * python index:i
    * left:2i+1
    * right:2i+2
    
    
# Week7    
## Merge Sort


## Binary Tree




