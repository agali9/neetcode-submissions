class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        l,r= 1, m
        out = 0
        while l<r:
            mid = (l+r)//2
            hours=0
            for i in piles: hours+= math.ceil(i/mid)
            if hours > h: l = mid+1
            else:
                r = mid
        return l