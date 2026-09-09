class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            p[i]*=prefix
            prefix*=nums[i]
        
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            p[i]*=suffix
            suffix*=nums[i]
        return p
