from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ptrs = deque(maxlen=k)
        count = 0
        mx = 0
        for i, elem in enumerate(nums):
            if elem == 1:
                count += 1
                mx = max(count, mx)
            elif len(ptrs) < k:
                ptrs.append(i)
                count += 1
                mx = max(count, mx)
            elif k == 0:
                count = 0
            else:
                loss = ptrs.popleft()
                ptrs.append(i)
                count = i - loss
                mx = max(mx, count)
        return mx
