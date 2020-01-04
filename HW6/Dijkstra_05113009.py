class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.tempp = {}
        self.temp = []
    def addEdge(self,u,v,w): 
        self.tempp.setdefault('%d-%d'%(u,v),w)
        self.temp.append([u,v,w])
        
        """
        :type u,v,w: int
        :rtype: None
        """
    def Dijkstra(self, s): 
        temp1 = [float('inf') if i == 0 else i for i in self.graph[s]]
        minone = min(temp1)
        temp1[s] = 0
        temp2 = [s] # 走訪過的點
        idx1 = temp1.index(minone)
        
        while len(temp2) < self.V:
            temp2.append(idx1)
            for i in range(self.V):
                if self.graph[idx1][i] != 0 and temp1[i] == float('inf'):
                    temp1[i] = self.graph[idx1][i] + temp1[idx1]

                if self.graph[idx1][i] != 0 and temp1[i] != float('inf') and self.graph[idx1][i] + temp1[idx1] < temp1[i]:
                    temp1[i] = self.graph[idx1][i] + temp1[idx1]
                    
            a = [i for i in temp1]
            minone = min(a)
            idx1 = a.index(minone)
            while idx1  in temp2 and a:
                a.remove(minone)
                if a:
                    minone = min(a)
                    idx1 = temp1.index(minone)
        
        output = {}
        for i,x in zip(range(self.V), temp1):
            output['%d'%i] = x
            
        return output
                             
        
        """
        :type s: int
        :rtype: dict
        """
    def Kruskal(self):
        temp = self.temp
        sort_temp = sorted(temp, key=lambda x:x[2]) #dict.values()排序
        parent = [-1]*self.V
        outlist = []
        
        root = sort_temp[0][0]
        n2 = sort_temp[0][1]
        parent[n2] = root
        visited = [root,n2]
        outlist.append(sort_temp[0])

        
        for i in range(1,len(sort_temp)):
            n1 = sort_temp[i][0]
            n2 = sort_temp[i][1]
            
            if n1 in visited and n2 in visited:
                if parent[n1] == parent[n2] and parent[n1] != -1:
                    continue
                    
                if n1 == root or n2 == root:
                    if n1 == root:
                        if parent[n2] == root:
                            continue
                            
                        parent = self.change_p_r(n1,n2,parent)   
                        outlist.append(sort_temp[i])
                        continue
                        
                    if n2 == root:
                        if parent[n1] == root:
                            continue
                            
                        parent = self.change_p_r(n2,n1,parent)
                        outlist.append(sort_temp[i])
                        continue
                        
                else: 
                    
                    if parent[n1] == root:
                        parent = self.changeparent(n1,n2,parent)
                        outlist.append(sort_temp[i])
                        continue  
                        
                    if parent[n2] == root:
                        parent = self.changeparent(n2,n1,parent)
                        outlist.append(sort_temp[i])
                        continue
                        
                    parent = self.changeparent(n1,n2,parent)
                    outlist.append(sort_temp[i])
                    continue
                    
                    
            if n1 == root:
                parent[n2] = parent[n1]
                visited.append(n2)
                outlist.append(sort_temp[i])
                continue
            
            if n2 == root:
                parent[n1] = parent[n2]
                visited.append(n1)
                outlist.append(sort_temp[i])
                continue
            
                    
            if n1 in visited or n2 in visited:
                if n1 in visited:
                    parent[n2] = parent[n1]
                    visited.append(n2)
                    outlist.append(sort_temp[i])
                    continue
                else:
                    parent[n1] = parent[n2]
                    visited.append(n1)
                    outlist.append(sort_temp[i])
                    continue                   
                               
            parent[n2] = n1
            visited.append(n1)
            visited.append(n2)
            outlist.append(sort_temp[i])
                               
        output = {}
        for i,j,x in outlist :
            if i > j:
                a = i
                i = j
                j = a
            output['%d-%d'%(i,j)] = x
        return(output)
             
        
        """
        :rtype: dict
        """
    
    def changeparent(self,a,b,parent):
        a = parent[a]
        if parent[b] == -1:
            parent[b] = a
            parent = [a if i == b else i for i in parent]
            
        else:
            np = parent[b]
            parent[np] = a
            parent = [a if i == np else i for i in parent]
        
        return parent
    
    def change_p_r(self,a,b,parent):
        if parent[b] == -1:
            parent[b] = a
            parent = [a if i == b else i for i in parent]
            
        else:
            np = parent[b]
            parent[np] = a
            parent = [a if i == np else i for i in parent]
        
        return parent
    
    
    

#https://kk665403.pixnet.net/blog/post/403711283-%5Bpython%5D-python-dict字典基本操作教學(新增-修改- __程式碼-字典
#https://chusiang.gitbooks.io/using-python/Dictionary.html __程式碼-字典
#https://codertw.com/程式語言/370975/ __程式碼-字典
#https://www.cnblogs.com/muchengnanfeng/p/9810918.html __程式碼-字典最大值
#https://blog.gtwang.org/programming/python-iterate-through-multiple-lists-in-parallel/ ___程式碼zip
#https://www.lfhacks.com/tech/python-list-element-replace __程式碼建list
#https://segmentfault.com/a/1190000004959880 ___程式碼dict排序
