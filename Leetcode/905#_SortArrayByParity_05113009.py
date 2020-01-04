class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        temp=[]
        temp1=[]
        for i in range(len(A)):
            if A[i]%2==0:
                temp.append(A[i])
            else:
                temp1.append(A[i])
        temp.extend(temp1)
        return temp
