class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums)<1:
            return
        nums.sort()
        sum=0
        for i in range(0,len(nums),2):
            sum+=min(nums[i],nums[i+1])
        return sum
