class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        first_pt = 0
        s = 0
        for i in range(k):
            s += nums[i]
        mx = s
        for elem in nums[k:]:
            s += elem
            s -= nums[first_pt]
            first_pt += 1
            mx = max(s, mx)
        return mx/k