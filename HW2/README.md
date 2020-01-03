# Heap Sort
* 子節點不得比父節點大，若子節點較大，則與父節點換位
* 比較後，最頂端的父節點為此數列的最大值，將其取出放入暫存空間 
* 取出最大值後，再進行一次比較排序
* 直到將所有數值由大到小都取出後，數列即完成排序
[程式碼](#https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW2/heap_sort_05113009.py)
[學習歷程](#https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW2/heap%20sort%20流程圖、學習歷程與文字說明.pdf)
<br>
<br>

# Merge Sort
* 把數列對半拆解，直到每個數列都只剩一個數值
* 將拆解好的數列倆倆做比較，比較後再做合併
* 依此類推，直到所有數列都合併成一個數列，即完成排序
[程式碼](#https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW2/merge_sort_05113009.py)
[學習歷程](#https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW2/merge%20sort%20流程圖、學習歷程與文字說明.pdf)
<br>
<br>


時間複雜度  | Quick Sort | Heap Sort | Merge Sort | Insertion Sort | Seletion Sort| 
-------------|------------|-----------|------------|----------------|--------------|
Best Case    | NlogN      |NlogN |NlogN |N|N^2
Average Case | NlogN      |NlogN |NlogN |N^2|N^2
Worst Case   | N^2        |NlogN |NlogN |N^2|N^2

<br>
<br>
<br>


Merge Sort 和 Heap Sort 理論上來說處理排序所需的時間是相同的，所以兩者在 效率上來看，是沒有太大的差別。
不過Heap Sort有分兩種，分別是Max Heap和Min Heap，差別在於一個是將不能 比父節點大，一個是不能比父節點小，亦即一個是取出最大值，而另外一個則 是取最小值，其他的概念皆相同。
Merge Sort 和 Heap Sort 最大的差別是Merge Sort 是以陣列的形式表現與處理， 而Heap Sort 則是採用陣列的形式表現，但用二元樹的方式理解。

<br>
<br>
<br>
<br>
<br>

## 流程圖
<img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW2/圖/heap%20sort%20圖.png" width="50%">  <img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW2/圖/merge%20sort%20圖.png" width="50%">

