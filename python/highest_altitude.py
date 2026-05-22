class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = mx = 0
        for elem in gain:
            curr += elem
            mx = max(curr, mx)
        return mx