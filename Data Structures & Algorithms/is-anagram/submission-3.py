class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for x in s:
            count[x] = count.get(x,0)+1
        for x in t:
            count[x] = count.get(x,0)-1
        return all(v == 0 for v in count.values())