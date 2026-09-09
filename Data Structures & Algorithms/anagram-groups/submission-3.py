class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            ch = [0]*26
            for c in s:
                ch[ord(c)-ord('a')]+=1
            hmap[tuple(ch)].append(s)
        return list(hmap.values())