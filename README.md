# DATA-STRUCTURES-AND-ALGORITHMS
* [Quick Sort](#quick-sort)
    * [過程](#過程)
    * [過程(另外存取空間)](#過程另外存取空間)
* [Heap Sort](#heap-sort)\


## Quick Sort
**快速排序法**，先決定取一個固定的位子為pivot，再依序將其餘的數值與pivot比大小，將比pivot小的都丟掉左邊，比pivot大的都丟到右邊。 再來將比pivot小的那些數值再比一次大小，並一樣取第一個為pivot，比pivot大的也用同樣的方式處理，直到不能再處理，亦即所有數值都依照大小都排好了。
[Quick Sort 程式碼](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW_Quick%20Sort/Quick%20Sort.ipynb)

### 過程
['54',26,93,17,77,31,44,55,20] --> list[left]=93, list[right]=20 --> 交換位置變成['54',26,20,17,77,31,44,55,93] --> list[left]=77, list[right]=44 -->交換位置變成['54',26,20,17,44,31,77,55,93] --> list[left]=77, list[right]=31 --> right < left --> pivot與list[right]交換值 --> [31,26,20,17,44,'54' ,77,55,93] 

-->第一次排序完成，接著再將小於54的數列依照此法排序，大於54的數列也是如此，最後就會得出依照大小排序好的 [17, 20, 26, 31, 44, 54, 55, 77, 93]

![](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW_Quick%20Sort/Quick%20Sort%20Demo.jpg)

### 過程(另外存取空間)
>['54',26,93,17,77,31,44,55,20] --> small=[26,17,31,44,20] , big=[93,77,55] , pivotlist=[54] 
>>['26',17,31,44,20] --> small=[17,20] , big=[31,44] , pivotlist=[26] --> return small + pivotlist + big --> [17,20,26,31,44] 
>>['93',77,55] --> small=[77,55] , big=[] , pivotlist=[93] <br/>
>>>['77',55] --> small=[55] , big=[] , pivotlist=[77] --> [55,77]
>>>>[55,77,93]\
return small + pivotlist + big --> [17, 20, 26, 31, 44, 54, 55, 77, 93]
<br>
<br>

## Heap Sort
### ***以陣列的形式表現，但要以二元樹的放式理解。***
每個子結點都必須小於父節點，當子結點大於父結點時，兩者交換位置，直到所有子結點都小於父結點，並且在最後將第一個結點拿出來，再將最後一個結點移到最前面，繼續進行排序，直到排序結束。<br>

![](https://algorithm.yuanbin.me/shared-files/images/Heapsort-example.gif)
