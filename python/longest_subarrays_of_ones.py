from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ptrs = deque(maxlen=1)
        count = 0
        mx = 0
        for i, elem in enumerate(nums):
            if elem == 1:
                count += 1
                mx = max(count, mx)
            elif not ptrs:
                ptrs.append(i)
            else:
                loss = ptrs.popleft()
                ptrs.append(i)
                print(f'{i=}, {loss=}')
                count = (i - loss) - 1
                mx = max(mx, count)
        if mx == len(nums):
            mx -= 1
        return mx