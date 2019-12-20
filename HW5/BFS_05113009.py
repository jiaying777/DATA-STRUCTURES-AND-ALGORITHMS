from collections import defaultdict 
  
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        temp1 = []
        temp1.extend(self.graph[s])
        temp2 = [s]
        if s in temp1:
            temp1.remove(s)

        while temp1 != []:
            fe = temp1[0]
            temp2.append(fe)
            temp1.remove(fe)
            for i in self.graph[fe]:
                if i not in temp1 and i not in temp2:
                    temp1.append(i)
        
        return temp2

        
    def DFS(self, s):
        temp1 = []
        temp1.extend(self.graph[s])
        temp2 = [s]
        if s in temp1:
            temp1.remove(s)
        
        while temp1 != []:
            le = temp1.pop()
            temp2.append(le)
            for i in self.graph[le]:
                if i not in temp1 and i not in temp2:
                    temp1.append(i)
                    
        return temp2


# https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7aa022d8bc_2_5
# http://codepad.org/bIExbqAn
# https://codertw.com/程式語言/365414/
