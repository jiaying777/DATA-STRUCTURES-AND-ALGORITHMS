class Solution(object):
        
    def heap_sort(self,list):

        self.heapsort(list)
        templist=[]
        templist.insert(0,list[0])
        for i in range(len(list)-1):
            list[0] = list[-1]
            list = list[:-1]
            self.heapsort(list)
            templist.insert(0,list[0])
        return templist
    
    def heapsort(self,list):
        change = False
        if len(list) <= 1:
            done = False  

        else:    
            done = True
            i = 0

        while done is True:
                if list[2*i+1] > list[i] :
                    temp = list[i]
                    list[i] = list[2*i+1]
                    list[2*i+1] = temp
                    change = True

                if len(list)>=3:
                    if list[2*i+2] > list[i] :
                        temp = list[i]
                        list[i] = list[2*i+2]
                        list[2*i+2] = temp
                        d1 = True
                        change = True

                i += 1

                if 2*i+1 > len(list)-1 :
                    done = False

                if 2*i+2 > len(list)-1 :
                    done = False

        if change == True:
            self.heapsort(list)

