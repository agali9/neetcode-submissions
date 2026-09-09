class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        for i in range(len(nums)-1):
            res[i+1] = res[i]*nums[i]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=right
            right*=nums[i]
        return res