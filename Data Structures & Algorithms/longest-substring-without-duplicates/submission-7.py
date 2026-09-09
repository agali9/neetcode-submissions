class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        m = 0
        l,r = 0,1
        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l+=1
            c.add(s[r])
            m = max(m,r-l+1)
        return m
