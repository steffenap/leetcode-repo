class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for elem in nums[1:]:
            res.append(elem + res[-1])
        return res
