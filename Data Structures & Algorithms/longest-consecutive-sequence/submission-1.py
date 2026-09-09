class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list1 = set(nums)
        m=0
        for n in list1:
            count = 0
            if n-1 not in list1:
                i = n
                while i in list1:
                    count+=1
                    i+=1
                m = max(m,count)
        return m