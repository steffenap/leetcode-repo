from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ctr = dict(Counter(nums))
        ops = 0
        seen = set()
        for key, val in ctr.items():
            if key not in seen:
                if key != (k - key):
                    ops += min(val, ctr.get((k - key), 0))
                else:
                    ops += ctr.get(key, 0) // 2
            seen.add(key)
            seen.add(k - key)
        return ops