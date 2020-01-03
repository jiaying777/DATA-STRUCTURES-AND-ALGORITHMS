#Quick Sort
[學習歷程](https://nbviewer.jupyter.org/github/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW1/Quick%20Sort%20程式碼與學習歷程.ipynb)<br>
[程式碼](https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/HW1/Quick_Sort_05113009.py)
<br/><br/><br/><br/><br/>

Quick Sort 快速排序法，先決定取一個固定的位子為pivot，再依序將其餘的數值與pivot比大小，將比pivot小的都丟掉走邊，比pivot大的都丟到右邊。 再來將比pivot小的那些數值再比一次大小，並一樣取第一個為pivot，比pivot大的也用同樣的方式處理，直到不能再處理，亦即所有數值都依照大小都排好了。

<br>

時間複雜度  | Quick Sort | Heap Sort | Merge Sort | Insertion Sort | Seletion Sort| 
-------------|------------|-----------|------------|----------------|--------------|
Best Case    | NlogN      |NlogN |NlogN |N|N^2
Average Case | NlogN      |NlogN |NlogN |N^2|N^2
Worst Case   | N^2        |NlogN |NlogN |N^2|N^2

<br>

## 流程圖
<img src="https://github.com/jiaying777/DATA-STRUCTURES-AND-ALGORITHMS/blob/master/圖/Quick%20Sort%20Demo.jpg" width="70%" >

