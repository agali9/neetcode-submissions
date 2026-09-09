class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dupe = set()

        for i in nums:
            no_dupe.add(i)
        return len(no_dupe)!=len(nums)