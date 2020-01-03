def quicksort(list):
    if len(list) <= 1: #若是list只有一個值，則不須比較大小直接回傳
        return list
    
    pivotlist= []
    left = []
    right = []

    pivot = list[0] #固定設第一個位置為pivot
    for i in list:
        if i < pivot: 
            left.append(i)#較小的放一邊
        if i > pivot: 
            right.append(i)#較大的放一邊
        if i == pivot:
            pivotlist.append(i)
                
    left = quicksort(left)
    right = quicksort(right)
    
    return left + pivotlist + right
    
#http://jialin128.pixnet.net/blog/post/142927691-%5B-資料結構-%5D-快速排序法（quick-sort）in-python
