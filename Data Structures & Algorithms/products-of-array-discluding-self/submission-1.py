class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            left = 1 
            right = 1
            for j in range(len(nums)):
                if j<i:
                    left*=nums[j]
                elif j>i:
                    right*=nums[j]
            products.append(left*right)
        return products