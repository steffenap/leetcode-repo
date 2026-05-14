class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        orig = len(nums)
        nums[:] = [x for x in nums if x != 0]
        diff = orig - len(nums)
        for i in range(diff):
            nums.append(0)