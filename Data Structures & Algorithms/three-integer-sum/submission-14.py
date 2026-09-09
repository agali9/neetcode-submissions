class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l<r:
                add = nums[i] + nums[l] + nums[r]
                if add == 0 and [nums[i],nums[l],nums[r]] not in out: 
                    out.append([nums[i],nums[l],nums[r]])
                elif add>0: r-=1
                else: l+=1
        return out