class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        m=1000000000000000000
        while l<=r:
            mid=(l+r)//2
            m = min(m,nums[mid])
            if nums[mid]>nums[len(nums)-1]:
                l = mid+1
            else:
                r=mid-1
        return m