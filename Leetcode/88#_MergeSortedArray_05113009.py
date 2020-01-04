class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n!=0:
            j=0
            k=0
            n1=nums1[:m]
            for i in range(m+n):
                if j>n-1:
                    continue
                if  k>=m:
                    nums1[i] = nums2[j]
                    j+=1
                    continue
                if  n1[k]<=nums2[j]:
                    k+=1
                    continue
                else:
                    nums1.insert(i,nums2[j])
                    j+=1
                    nums1.pop()
