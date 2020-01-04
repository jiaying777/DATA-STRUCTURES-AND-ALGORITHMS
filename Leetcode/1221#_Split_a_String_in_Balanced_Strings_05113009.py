class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        a=s[0]
        ca=1
        for i in range(1,len(s)):
            if a == s[i]:
                ca+=1
                continue
            else:
                ca-=1
                if ca==0:
                    count+=1
                    if i+1 < len(s)-1:
                        a=s[i+1]
        return count
