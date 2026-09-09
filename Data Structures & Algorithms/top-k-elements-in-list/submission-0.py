from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        m = dict(sorted(m.items(),key=itemgetter(1), reverse=True))
        return list(m.keys())[:k]
