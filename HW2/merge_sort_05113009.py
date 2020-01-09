class Solution(object):
    def merge_sort(self,list):
    
        if len(list) <= 1: #新增條件，避免錯誤
            return list
        if len(list) > 1:
            list1,list2 = self.split(list)
        if len(list1) > 1:
            list1 = self.merge_sort(list1)
        if len(list2) > 1:
            list2 = self.merge_sort(list2)
        i = 0
        l = 0
        r = 0
        a = float('inf')
        array = []
        list1.append(a)
        list2.append(a)
        for i in range(len(list1)+len(list2)-2):
            if list1[l]<=list2[r] :
                array.append(list1[l])
                l += 1
            else :
                array.append(list2[r])
                r += 1
        list = array
        return list
    
    def split(self,list):
        if len(list) > 1:
            list1 = list[:round(len(list)/2)]
            list2 = list[round(len(list)/2):]
            
        return list1,list2
