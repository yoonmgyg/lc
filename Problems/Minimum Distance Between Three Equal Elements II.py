class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)

        hm = {}
        pre = [-1]*n
        for i in range(n):
            if nums[i] not in hm:
                hm[nums[i]] = i 
            else:
                pre[i] = hm[nums[i]]
                hm[nums[i]] = i 

        hm = {}
        suf = [-1]*n 
        for i in range(n-1,-1,-1):
            if nums[i] not in hm:
                hm[nums[i]] = i 
            else:
                suf[i] = hm[nums[i]]
                hm[nums[i]] = i 

        ans = float('inf')
        for i in range(1,n-1):
            if pre[i]!=-1 and suf[i]!=-1:
                a,b,c = pre[i],i,suf[i]
                ans = min(ans,(abs(a-b)+abs(b-c)+abs(c-a)))

        if ans==float('inf'):
            return -1
        return ans
                
                
