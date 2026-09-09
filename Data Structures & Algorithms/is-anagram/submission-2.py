class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for x in s:
            if x not in map1:
                map1[x] = 0
            map1[x]+=1
        for x in t:
            if x not in map2:
                map2[x] = 0
            map2[x]+=1
        return map1 == map2