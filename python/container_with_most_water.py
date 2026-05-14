class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        l = 0
        r = len(height) - 1
        while r > l:
            w = r - l
            h = min(height[l], height[r])
            curr = w * h
            max_val = max(max_val, curr)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_val